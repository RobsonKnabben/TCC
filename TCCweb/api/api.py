# coding: utf-8
from tastypie.resources import ModelResource
from tastypie import fields
from TCCweb.appAdmin.models import Ramo, Estabelecimento, Produto, Linha, Telefone


class RamoResource(ModelResource):
    class Meta:
        queryset=Ramo.objects.all()
        resource_name='ramos'
        #fields = ['username', 'first_name', 'last_name', 'last_login']
        allowed_methods = ['get']
        include_resource_uri=False
        limit=1000

    def determine_format(self, request):
        return 'application/json'


class EstabelecimentoResource(ModelResource):
    # ramo = fields.ToManyField('TCCweb.core.api.RamoResource', 'ramo', full=True)
    class Meta:
        queryset=Estabelecimento.objects.all()
        resource_name='estabelecimentos'
        #fields = ['username', 'first_name', 'last_name', 'last_login']
        allowed_methods = ['get']
        include_resource_uri=False
        limit=1000

    def determine_format(self, request):
        return 'application/json'


class ProdutoResource(ModelResource):
    class Meta:
        queryset=Produto.objects.all()
        resource_name='produtos'
        #fields = ['username', 'first_name', 'last_name', 'last_login']
        allowed_methods = ['get']
        include_resource_uri=False
        limit=1000

    def determine_format(self, request):
        return 'application/json'


class LinhaResource(ModelResource):
    class Meta:
        queryset=Linha.objects.all()
        resource_name='linhas'
        #fields = ['username', 'first_name', 'last_name', 'last_login']
        allowed_methods = ['get']
        include_resource_uri=False
        limit=1000

    def determine_format(self, request):
        return 'application/json'

class TelefoneResource(ModelResource):
    class Meta:
        queryset=Telefone.objects.all()
        resource_name='telefones'
        #fields = ['username', 'first_name', 'last_name', 'last_login']
        allowed_methods = ['get']
        include_resource_uri=False
        limit=1000

    def determine_format(self, request):
        return 'application/json'