# coding: utf-8
from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import User
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes import generic
from django.db.models.signals import post_save


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
    ramo = models.ManyToManyField(Ramo)

    @property
    def telefones(self):
        return Telefone.objects.filter(estabelecimento=self)

    @property
    def produtos(self):
        return Produto.objects.filter(estabelecimento=self)

    class Meta:
        ordering = [u'name']
        verbose_name = _(u'estabelecimento')
        verbose_name_plural = _(u'estabelecimentos')

    def __unicode__(self):
        return self.name


class Telefone(models.Model):
    numero = models.CharField(_('Telefone'), max_length=20, blank=True)
    estabelecimento = models.ForeignKey(Estabelecimento, editable=False)

    class Meta:
        ordering = [u'numero']
        verbose_name = _(u'telefone')
        verbose_name_plural = _(u'telefones')

    def __unicode__(self):
        return self.numero


class Linha(models.Model):
    name = models.CharField(_('Nome'), max_length=50, blank=False)
    estabelecimento = models.ForeignKey(Estabelecimento, editable=False)

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
    linha = models.ForeignKey(Linha)
    estabelecimento = models.ForeignKey(Estabelecimento, editable=False)
    inativo = models.BooleanField()

    class Meta:
        ordering = [u'name']
        verbose_name = _(u'produto')
        verbose_name_plural = _(u'produtos')

    def __unicode__(self):
        return self.name


class UserProfile(models.Model):
    user = models.OneToOneField(User)
    estabelecimento = models.OneToOneField(Estabelecimento, null=True, unique=True)


def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)

post_save.connect(create_user_profile, sender=User)