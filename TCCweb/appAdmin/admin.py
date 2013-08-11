# coding: utf-8
from django.contrib import admin
from TCCweb.appAdmin.models import Estabelecimento, Produto, Linha, Telefone, Ramo, UserProfile

from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User


class TelefoneInline(admin.TabularInline):
    model = Telefone
    extra = 1
    varbose_name_plural = 'telefones'


class EstabelecimentoAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', )
    search_fields = ('name',)
    inlines = (TelefoneInline, )

    def queryset(self, request):
        qs = super(EstabelecimentoAdmin, self).queryset(request)
        if request.user.is_superuser:
            return qs
        elif not request.user.get_profile().estabelecimento:
            return qs.filter(id=-1)
        return qs.filter(id=request.user.get_profile().estabelecimento.id)


class RamoAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)


class TelefoneAdmin(admin.ModelAdmin):
    list_display = ('numero', 'estabelecimento')
    search_fields = ('numero',)

    def queryset(self, request):
        qs = super(TelefoneAdmin, self).queryset(request)
        return qs.filter(estabelecimento=request.user.get_profile().estabelecimento)

    def save_model(self, request, obj, form, change):
        if request.user.get_profile().estabelecimento:
            obj.estabelecimento=request.user.get_profile().estabelecimento
            obj.save()


class ProdutoAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'linha', 'price', 'inativo')
    search_fields = ('name',)

    def formfield_for_foreignkey(self, db_field, request=None, **kwargs):
        if db_field.name == 'linha':
            kwargs['queryset'] = Linha.objects.filter(estabelecimento=request.user.get_profile().estabelecimento)
            return db_field.formfield(**kwargs)
        return super(ProdutoAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

    def queryset(self, request):
        qs = super(ProdutoAdmin, self).queryset(request)
        return qs.filter(estabelecimento=request.user.get_profile().estabelecimento)

    def save_model(self, request, obj, form, change):
        if request.user.get_profile().estabelecimento:
            obj.estabelecimento=request.user.get_profile().estabelecimento
            obj.save()


class LinhaAdmin(admin.ModelAdmin):
    list_display = ('name', 'estabelecimento')
    search_fields = ('name',)

    def queryset(self, request):
        qs = super(LinhaAdmin, self).queryset(request)
        return qs.filter(estabelecimento=request.user.get_profile().estabelecimento)

    def save_model(self, request, obj, form, change):
        if request.user.get_profile().estabelecimento:
            obj.estabelecimento=request.user.get_profile().estabelecimento
            obj.save()


class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'estabelecimento')
    search_fields = ('user','estabelecimento')


admin.site.unregister(User)

admin.site.register(User, UserAdmin)
admin.site.register(Estabelecimento, EstabelecimentoAdmin)
admin.site.register(Produto, ProdutoAdmin)
admin.site.register(Linha, LinhaAdmin)
admin.site.register(Telefone, TelefoneAdmin)
admin.site.register(Ramo, RamoAdmin)
admin.site.register(UserProfile, UserProfileAdmin)