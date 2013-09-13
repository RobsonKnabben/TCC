# coding: utf-8
from tastypie.resources import ModelResource
from tastypie import fields
from TCCweb.appAdmin.models import Ramo, Estabelecimento, Produto, Linha, Telefone
import copy

class RamoResource(ModelResource):
    class Meta:
        queryset=Ramo.objects.all()
        resource_name='ramos'
        fields = ['id', 'name', 'deleted',]
        allowed_methods = ['get']
        include_resource_uri=False

        filtering = {'name':('exact',),}

    def alter_list_data_to_serialize(self, request, data_dict):
        if isinstance(data_dict, dict):
            if 'meta' in data_dict:
                del(data_dict['meta'])
                data_dict = copy.copy(data_dict['objects'])
        return data_dict

    def determine_format(self, request):
        return 'application/json'


class EstabelecimentoResource(ModelResource):
    linhas = fields.OneToManyField('TCCweb.api.api.LinhaResource', 'linhas', full=True)
    telefones = fields.OneToManyField('TCCweb.api.api.TelefoneResource', 'telefones', full=True)
    ramos = fields.OneToManyField('TCCweb.api.api.RamoResource', 'ramo', full=True)

    class Meta:
        queryset=Estabelecimento.objects.all()
        resource_name='estabelecimentos'
        fields = ['id', 'name', 'description', 'inativo', 'deleted']
        allowed_methods = ['get']
        include_resource_uri=False
        filtering = {
            'id':('exact',),
            'name':('exact',),
            }

    def alter_list_data_to_serialize(self, request, data_dict):
        if isinstance(data_dict, dict):
            if 'meta' in data_dict:
                del(data_dict['meta'])
                data_dict = copy.copy(data_dict['objects'])
        return data_dict

    def determine_format(self, request):
        return 'application/json'


class TelefoneResource(ModelResource):
    class Meta:
        queryset=Telefone.objects.all()
        resource_name='telefones'
        #fields = ['username', 'first_name', 'last_name', 'last_login']
        allowed_methods = ['get']
        include_resource_uri=False

    def alter_list_data_to_serialize(self, request, data_dict):
        if isinstance(data_dict, dict):
            if 'meta' in data_dict:
                del(data_dict['meta'])
                data_dict = copy.copy(data_dict['objects'])
        return data_dict

    def determine_format(self, request):
        return 'application/json'


class ProdutoResource(ModelResource):
    class Meta:
        queryset=Produto.objects.all()
        resource_name='produtos'
        #fields = ['username', 'first_name', 'last_name', 'last_login']
        allowed_methods = ['get']
        include_resource_uri=False

    def alter_list_data_to_serialize(self, request, data_dict):
        if isinstance(data_dict, dict):
            if 'meta' in data_dict:
                # Get rid of the "meta".
                del(data_dict['meta'])
                # Rename the objects.
                #data_dict['produtos'] = copy.copy(data_dict['objects'])
                data_dict = copy.copy(data_dict['objects'])
                #del(data_dict['objects'])
        return data_dict

    def determine_format(self, request):
        return 'application/json'


class LinhaResource(ModelResource):
    produtos = fields.OneToManyField('TCCweb.api.api.ProdutoResource', 'produtos', full=True)

    class Meta:
        queryset=Linha.objects.all()
        resource_name='linhas'
        #fields = ['username', 'first_name', 'last_name', 'last_login']
        allowed_methods = ['get']
        include_resource_uri=False

    def alter_list_data_to_serialize(self, request, data_dict):
        if isinstance(data_dict, dict):
            if 'meta' in data_dict:
                del(data_dict['meta'])
                data_dict = copy.copy(data_dict['objects'])
        return data_dict

    def determine_format(self, request):
        return 'application/json'