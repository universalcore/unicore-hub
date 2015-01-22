# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'ServiceTicket'
        db.create_table(u'mama_cas_serviceticket', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('ticket', self.gf('django.db.models.fields.CharField')(unique=True, max_length=255)),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'])),
            ('expires', self.gf('django.db.models.fields.DateTimeField')()),
            ('consumed', self.gf('django.db.models.fields.DateTimeField')(null=True)),
            ('service', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('primary', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal(u'mama_cas', ['ServiceTicket'])

        # Adding model 'ProxyTicket'
        db.create_table(u'mama_cas_proxyticket', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('ticket', self.gf('django.db.models.fields.CharField')(unique=True, max_length=255)),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'])),
            ('expires', self.gf('django.db.models.fields.DateTimeField')()),
            ('consumed', self.gf('django.db.models.fields.DateTimeField')(null=True)),
            ('service', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('granted_by_pgt', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['mama_cas.ProxyGrantingTicket'])),
        ))
        db.send_create_signal(u'mama_cas', ['ProxyTicket'])

        # Adding model 'ProxyGrantingTicket'
        db.create_table(u'mama_cas_proxygrantingticket', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('ticket', self.gf('django.db.models.fields.CharField')(unique=True, max_length=255)),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'])),
            ('expires', self.gf('django.db.models.fields.DateTimeField')()),
            ('consumed', self.gf('django.db.models.fields.DateTimeField')(null=True)),
            ('iou', self.gf('django.db.models.fields.CharField')(unique=True, max_length=255)),
            ('granted_by_st', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['mama_cas.ServiceTicket'], null=True, on_delete=models.PROTECT, blank=True)),
            ('granted_by_pt', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['mama_cas.ProxyTicket'], null=True, on_delete=models.PROTECT, blank=True)),
        ))
        db.send_create_signal(u'mama_cas', ['ProxyGrantingTicket'])


    def backwards(self, orm):
        # Deleting model 'ServiceTicket'
        db.delete_table(u'mama_cas_serviceticket')

        # Deleting model 'ProxyTicket'
        db.delete_table(u'mama_cas_proxyticket')

        # Deleting model 'ProxyGrantingTicket'
        db.delete_table(u'mama_cas_proxygrantingticket')


    models = {
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
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Group']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Permission']"}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'mama_cas.proxygrantingticket': {
            'Meta': {'object_name': 'ProxyGrantingTicket'},
            'consumed': ('django.db.models.fields.DateTimeField', [], {'null': 'True'}),
            'expires': ('django.db.models.fields.DateTimeField', [], {}),
            'granted_by_pt': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['mama_cas.ProxyTicket']", 'null': 'True', 'on_delete': 'models.PROTECT', 'blank': 'True'}),
            'granted_by_st': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['mama_cas.ServiceTicket']", 'null': 'True', 'on_delete': 'models.PROTECT', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'iou': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '255'}),
            'ticket': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '255'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']"})
        },
        u'mama_cas.proxyticket': {
            'Meta': {'object_name': 'ProxyTicket'},
            'consumed': ('django.db.models.fields.DateTimeField', [], {'null': 'True'}),
            'expires': ('django.db.models.fields.DateTimeField', [], {}),
            'granted_by_pgt': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['mama_cas.ProxyGrantingTicket']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'service': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'ticket': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '255'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']"})
        },
        u'mama_cas.serviceticket': {
            'Meta': {'object_name': 'ServiceTicket'},
            'consumed': ('django.db.models.fields.DateTimeField', [], {'null': 'True'}),
            'expires': ('django.db.models.fields.DateTimeField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'primary': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'service': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'ticket': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '255'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']"})
        }
    }

    complete_apps = ['mama_cas']