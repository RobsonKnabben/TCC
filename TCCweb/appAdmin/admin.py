# coding: utf-8
from symbol import return_stmt
from django.contrib import admin
from TCCweb.appAdmin.models import Estabelecimento, Produto, Linha, Telefone, Ramo, UserProfile


from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User


class TelefoneAdmin(admin.ModelAdmin):
    list_display = ('numero', 'estabelecimento')
    search_fields = ('numero',)

    def queryset(self, request):
        return super(TelefoneAdmin, self).queryset(request).filter(estabelecimento=request.user.get_profile().estabelecimento)

    def save_model(self, request, obj, form, change):
        obj.estabelecimento=request.user.get_profile().estabelecimento
        obj.save()


class TelefoneInline(admin.TabularInline):
    model = Telefone
    extra = 1
    varbose_name_plural = 'Telefones'


class EstabelecimentoAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', )
    search_fields = ('name',)
    inlines = (TelefoneInline, )
    def queryset(self, request):
        if request.user.is_superuser:
            return super(EstabelecimentoAdmin, self).queryset(request)
        return super(EstabelecimentoAdmin, self).queryset(request).filter(id=request.user.get_profile().estabelecimento.id)


class ProdutoAdmin(admin.ModelAdmin):
    list_display = ('name', 'description','price', 'inativo')
    search_fields = ('name',)


    def queryset(self, request):
        return super(ProdutoAdmin, self).queryset(request).filter(estabelecimento=request.user.get_profile().estabelecimento)

    def save_model(self, request, obj, form, change):
        obj.estabelecimento=request.user.get_profile().estabelecimento
        obj.save()


class LinhaAdmin(admin.ModelAdmin):
    list_display = ('name', 'estabelecimento')
    search_fields = ('name',)

    def queryset(self, request):
        return super(LinhaAdmin, self).queryset(request).filter(estabelecimento=request.user.get_profile().estabelecimento)

    def save_model(self, request, obj, form, change):
        obj.estabelecimento=request.user.get_profile().estabelecimento
        obj.save()


class RamoAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)


class UserProfileInline(admin.StackedInline):
    model = UserProfile
    can_delete = False
    verbose_name_plural = 'profile'


class UserAdmin(UserAdmin):
    inlines = (UserProfileInline, )



admin.site.unregister(User)

admin.site.register(User, UserAdmin)
admin.site.register(Estabelecimento, EstabelecimentoAdmin)
admin.site.register(Produto, ProdutoAdmin)
admin.site.register(Linha, LinhaAdmin)
admin.site.register(Telefone, TelefoneAdmin)
admin.site.register(Ramo, RamoAdmin)