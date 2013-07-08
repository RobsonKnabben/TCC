# coding: utf-8
from django.conf.urls import patterns, include, url
from api import RamoResource, EstabelecimentoResource, ProdutoResource, LinhaResource, TelefoneResource


ramo_resource = RamoResource()
estabelecimento_resource = EstabelecimentoResource()
produto_resource = ProdutoResource()
linha_resource = LinhaResource()
telefone_resource = TelefoneResource()

urlpatterns = patterns('',
    url(r'^', include(ramo_resource.urls)),
    url(r'^', include(estabelecimento_resource.urls)),
    url(r'^', include(produto_resource.urls)),
    url(r'^', include(linha_resource.urls)),
    url(r'^', include(telefone_resource.urls)),
)
