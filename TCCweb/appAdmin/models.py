# coding: utf-8
from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from tastypie.fields import OneToManyField


class Ramo(models.Model):
    name = models.CharField(_('Nome'), max_length=50, blank=False)

    class Meta:
        ordering = [u'name']
        verbose_name = _(u'ramo')
        verbose_name_plural = _(u'ramos')

    def __unicode__(self):
        return self.name


class Estabelecimento(models.Model):
    name = models.CharField(_('Nome'), max_length=50)
    description = models.TextField(_(u'Descrição'), max_length=200)
    ramo = models.ManyToManyField(Ramo, related_name='estabelecimentos')

    class Meta:
        ordering = [u'name']
        verbose_name = _(u'estabelecimento')
        verbose_name_plural = _(u'estabelecimentos')

    def __unicode__(self):
        return self.name


class Telefone(models.Model):
    numero = models.CharField(_('Telefone'), max_length=20, blank=True)
    estabelecimento = models.ForeignKey(Estabelecimento, related_name='telefones', editable=False)

    class Meta:
        ordering = [u'numero']
        verbose_name = _(u'telefone')
        verbose_name_plural = _(u'telefones')

    def __unicode__(self):
        return self.numero


class Linha(models.Model):
    name = models.CharField(_('Nome'), max_length=50, blank=False)
    estabelecimento = models.ForeignKey(Estabelecimento, related_name='linhas', editable=False)

    class Meta:
        ordering = [u'name']
        verbose_name = _(u'linha')
        verbose_name_plural = _(u'linhas')

    def __unicode__(self):
        return self.name


class Produto(models.Model):
    name = models.CharField(_('Nome'), max_length=50)
    description = models.TextField(_(u'Descrição'), max_length=200)
    price = models.DecimalField(_(u'Preço'), max_digits=12, decimal_places=2)
    linha = models.ForeignKey(Linha, related_name='produtos')
    estabelecimento = models.ForeignKey(Estabelecimento, related_name='produtos', editable=False)
    inativo = models.BooleanField()

    class Meta:
        ordering = [u'name']
        verbose_name = _(u'produto')
        verbose_name_plural = _(u'produtos')

    def __unicode__(self):
        return self.name


class UserProfile(models.Model):
    user = models.OneToOneField(User)
    estabelecimento = models.OneToOneField(Estabelecimento, related_name='perfil', null=True, blank=True, unique=True)

    class Meta:
        ordering = [u'user']
        verbose_name = _(u'perfil')
        verbose_name_plural = _(u'perfis')

    def __unicode__(self):
        return unicode(self.user)


def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)

post_save.connect(create_user_profile, sender=User)