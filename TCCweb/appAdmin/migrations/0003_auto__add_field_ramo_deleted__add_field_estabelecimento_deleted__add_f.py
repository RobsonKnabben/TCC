# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Ramo.deleted'
        db.add_column(u'appAdmin_ramo', 'deleted',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)

        # Adding field 'Estabelecimento.deleted'
        db.add_column(u'appAdmin_estabelecimento', 'deleted',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)

        # Adding field 'Telefone.deleted'
        db.add_column(u'appAdmin_telefone', 'deleted',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)

        # Adding field 'Linha.deleted'
        db.add_column(u'appAdmin_linha', 'deleted',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Ramo.deleted'
        db.delete_column(u'appAdmin_ramo', 'deleted')

        # Deleting field 'Estabelecimento.deleted'
        db.delete_column(u'appAdmin_estabelecimento', 'deleted')

        # Deleting field 'Telefone.deleted'
        db.delete_column(u'appAdmin_telefone', 'deleted')

        # Deleting field 'Linha.deleted'
        db.delete_column(u'appAdmin_linha', 'deleted')


    models = {
        u'appAdmin.estabelecimento': {
            'Meta': {'ordering': "[u'name']", 'object_name': 'Estabelecimento'},
            'deleted': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'description': ('django.db.models.fields.TextField', [], {'max_length': '200'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'ramo': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'estabelecimentos'", 'symmetrical': 'False', 'to': u"orm['appAdmin.Ramo']"})
        },
        u'appAdmin.linha': {
            'Meta': {'ordering': "[u'name']", 'object_name': 'Linha'},
            'deleted': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'estabelecimento': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'linhas'", 'to': u"orm['appAdmin.Estabelecimento']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'appAdmin.produto': {
            'Meta': {'ordering': "[u'name']", 'object_name': 'Produto'},
            'deleted': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'description': ('django.db.models.fields.TextField', [], {'max_length': '200'}),
            'estabelecimento': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'produtos'", 'to': u"orm['appAdmin.Estabelecimento']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'inativo': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'linha': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'produtos'", 'to': u"orm['appAdmin.Linha']"}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'price': ('django.db.models.fields.DecimalField', [], {'max_digits': '12', 'decimal_places': '2'})
        },
        u'appAdmin.ramo': {
            'Meta': {'ordering': "[u'name']", 'object_name': 'Ramo'},
            'deleted': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'appAdmin.telefone': {
            'Meta': {'ordering': "[u'numero']", 'object_name': 'Telefone'},
            'deleted': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'estabelecimento': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'telefones'", 'to': u"orm['appAdmin.Estabelecimento']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'numero': ('django.db.models.fields.CharField', [], {'max_length': '15', 'blank': 'True'})
        },
        u'appAdmin.userprofile': {
            'Meta': {'ordering': "[u'user']", 'object_name': 'UserProfile'},
            'estabelecimento': ('django.db.models.fields.related.OneToOneField', [], {'blank': 'True', 'related_name': "'perfil'", 'unique': 'True', 'null': 'True', 'to': u"orm['appAdmin.Estabelecimento']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'user': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['auth.User']", 'unique': 'True'})
        },
        u'auth.group': {
            'Meta': {'object_name': 'Group'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        u'auth.permission': {
            'Meta': {'ordering': "(u'content_type__app_label', u'content_type__model', u'codename')", 'unique_together': "((u'content_type', u'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contenttypes.ContentType']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Group']", 'symmetrical': 'False', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        }
    }

    complete_apps = ['appAdmin']