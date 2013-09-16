# coding: utf-8
from django.contrib import admin
from TCCweb.appAdmin.models import Estabelecimento, Produto, Linha, Telefone, Ramo, UserProfile

from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from django.contrib.localflavor.br.forms import BRPhoneNumberField
from django.forms import ModelForm

DELETAR = True
MOSTRAR_DELETED = False


class TelefoneForm(ModelForm):
    numero = BRPhoneNumberField()

    class Meta:
        model = Telefone


class TelefoneInline(admin.TabularInline):
    model = Telefone
    extra = 1
    verbose_name = 'telefones'
    can_delete = False
    form = TelefoneForm

    def queryset(self, request):
        return super(TelefoneInline, self).queryset(request).filter(deleted=MOSTRAR_DELETED)


class EstabelecimentoAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', )
    search_fields = ('name',)
    inlines = (TelefoneInline, )

    actions = ['deletar_selecionados']

    def deletar_selecionados(self, request, queryset):
        for obj in queryset:
            obj.deleted=DELETAR
            for objeto in Produto.objects.all().filter(estabelecimento=obj):
                objeto.deleted=DELETAR
                objeto.save()
            for objeto in Linha.objects.all().filter(estabelecimento=obj):
                objeto.deleted=DELETAR
                objeto.save()
            for objeto in Telefone.objects.all().filter(estabelecimento=obj):
                objeto.deleted=DELETAR
                objeto.save()
            obj.save()

    deletar_selecionados.short_description = "Remover itens selecionados"

    def queryset(self, request):
        qs = super(EstabelecimentoAdmin, self).queryset(request)
        if request.user.is_superuser:
            return qs.filter(deleted=MOSTRAR_DELETED)
        elif not request.user.get_profile().estabelecimento:
            return qs.filter(id=-1)
        return qs.filter(id=request.user.get_profile().estabelecimento.id, deleted=MOSTRAR_DELETED)

    def get_form(self, request, obj=None, **kwargs):
        self.exclude = []
        if not request.user.is_superuser:
            self.exclude.append('inativo')
        return super(EstabelecimentoAdmin, self).get_form(request, obj, **kwargs)


    def delete_model(self, request, obj):
        obj.deleted=DELETAR
        for objeto in Produto.objects.all().filter(estabelecimento=obj):
            objeto.deleted=DELETAR
            objeto.save()
        for objeto in Linha.objects.all().filter(estabelecimento=obj):
            objeto.deleted=DELETAR
            objeto.save()
        for objeto in Telefone.objects.all().filter(estabelecimento=obj):
            objeto.deleted=DELETAR
            objeto.save()
        obj.save()



class RamoAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

    actions = ['deletar_selecionados']

    def deletar_selecionados(self, request, queryset):
        for obj in queryset:
            obj.deleted=DELETAR
            obj.save()
            for estabelecimento in Estabelecimento.objects.all().filter(ramo=obj):
                estabelecimento.deleted=DELETAR
                estabelecimento.save()
                for objeto in Produto.objects.all().filter(estabelecimento=estabelecimento):
                    objeto.deleted=DELETAR
                    objeto.save()
                for objeto in Linha.objects.all().filter(estabelecimento=estabelecimento):
                    objeto.deleted=DELETAR
                    objeto.save()
                for objeto in Telefone.objects.all().filter(estabelecimento=estabelecimento):
                    objeto.deleted=DELETAR
                    objeto.save()

    def queryset(self, request):
        qs = super(RamoAdmin, self).queryset(request)
        return qs.filter(deleted=MOSTRAR_DELETED)


    deletar_selecionados.short_description = "Remover itens selecionados"

    def delete_model(self, request, obj):
        obj.deleted=DELETAR
        obj.save()
        for estabelecimento in Estabelecimento.objects.all().filter(ramo=obj):
            estabelecimento.deleted=DELETAR
            estabelecimento.save()
            for objeto in Produto.objects.all().filter(estabelecimento=estabelecimento):
                objeto.deleted=DELETAR
                objeto.save()
            for objeto in Linha.objects.all().filter(estabelecimento=estabelecimento):
                objeto.deleted=DELETAR
                objeto.save()
            for objeto in Telefone.objects.all().filter(estabelecimento=estabelecimento):
                objeto.deleted=DELETAR
                objeto.save()


class TelefoneAdmin(admin.ModelAdmin):
    form = TelefoneForm
    list_display = ('numero', 'estabelecimento',)
    search_fields = ('numero',)

    actions = ['deletar_selecionados']

    def deletar_selecionados(self, request, queryset):
        for obj in queryset:
            obj.deleted=DELETAR
            obj.save()

    deletar_selecionados.short_description = "Remover itens selecionados"

    def queryset(self, request):
        qs = super(TelefoneAdmin, self).queryset(request)
        return qs.filter(estabelecimento=request.user.get_profile().estabelecimento, deleted=MOSTRAR_DELETED)

    def save_model(self, request, obj, form, change):
        if request.user.get_profile().estabelecimento:
            obj.estabelecimento=request.user.get_profile().estabelecimento
            obj.save()

    def delete_model(self, request, obj):
        obj.deleted=DELETAR
        obj.save()


class ProdutoAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'linha', 'price', 'inativo',)
    search_fields = ('name',)

    actions = ['deletar_selecionados']

    def deletar_selecionados(self, request, queryset):
        for obj in queryset:
            obj.deleted=DELETAR
            obj.save()

    deletar_selecionados.short_description = "Remover itens selecionados"

    def formfield_for_foreignkey(self, db_field, request=None, **kwargs):
        if db_field.name == 'linha':
            kwargs['queryset'] = Linha.objects.filter(estabelecimento=request.user.get_profile().estabelecimento)
            return db_field.formfield(**kwargs)
        return super(ProdutoAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

    def queryset(self, request):
        qs = super(ProdutoAdmin, self).queryset(request)
        return qs.filter(estabelecimento=request.user.get_profile().estabelecimento, deleted=MOSTRAR_DELETED)

    def save_model(self, request, obj, form, change):
        if request.user.get_profile().estabelecimento:
            obj.estabelecimento=request.user.get_profile().estabelecimento
            obj.save()

    def delete_model(self, request, obj):
        obj.deleted=DELETAR
        obj.save()


class LinhaAdmin(admin.ModelAdmin):
    list_display = ('name', 'estabelecimento',)
    search_fields = ('name',)

    actions = ['deletar_selecionados']

    def deletar_selecionados(self, request, queryset):
        for obj in queryset:
            obj.deleted=DELETAR
            for prod in Produto.objects.all().filter(linha=obj):
                prod.deleted=DELETAR
                prod.save()
            obj.save()

    deletar_selecionados.short_description = "Remover itens selecionados"

    def queryset(self, request):
        qs = super(LinhaAdmin, self).queryset(request)
        return qs.filter(estabelecimento=request.user.get_profile().estabelecimento, deleted=MOSTRAR_DELETED)

    def save_model(self, request, obj, form, change):
        if request.user.get_profile().estabelecimento:
            obj.estabelecimento=request.user.get_profile().estabelecimento
            obj.save()

    def delete_model(self, request, obj):
        obj.deleted=DELETAR
        for objeto in Produto.objects.all().filter(linha=obj):
            objeto.deleted=DELETAR
            objeto.save()
        obj.save()


class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'estabelecimento')
    search_fields = ('user','estabelecimento')


admin.site.disable_action('delete_selected')


admin.site.unregister(User)

admin.site.register(User, UserAdmin)
admin.site.register(Estabelecimento, EstabelecimentoAdmin)
admin.site.register(Produto, ProdutoAdmin)
admin.site.register(Linha, LinhaAdmin)
admin.site.register(Telefone, TelefoneAdmin)
admin.site.register(Ramo, RamoAdmin)
admin.site.register(UserProfile, UserProfileAdmin)