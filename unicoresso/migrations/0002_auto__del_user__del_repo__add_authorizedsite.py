# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting model 'User'
        db.delete_table(u'unicoresso_user')

        # Deleting model 'Repo'
        db.delete_table(u'unicoresso_repo')

        # Removing M2M table for field users on 'Repo'
        db.delete_table(db.shorten_name(u'unicoresso_repo_users'))

        # Adding model 'AuthorizedSite'
        db.create_table(u'unicoresso_authorizedsite', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('site', self.gf('django.db.models.fields.CharField')(max_length=200)),
        ))
        db.send_create_signal(u'unicoresso', ['AuthorizedSite'])

        # Adding M2M table for field group on 'AuthorizedSite'
        m2m_table_name = db.shorten_name(u'unicoresso_authorizedsite_group')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('authorizedsite', models.ForeignKey(orm[u'unicoresso.authorizedsite'], null=False)),
            ('group', models.ForeignKey(orm[u'auth.group'], null=False))
        ))
        db.create_unique(m2m_table_name, ['authorizedsite_id', 'group_id'])


    def backwards(self, orm):
        # Adding model 'User'
        db.create_table(u'unicoresso_user', (
            ('username', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('password', self.gf('django.db.models.fields.CharField')(max_length=30)),
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
        ))
        db.send_create_signal(u'unicoresso', ['User'])

        # Adding model 'Repo'
        db.create_table(u'unicoresso_repo', (
            ('url', self.gf('django.db.models.fields.CharField')(max_length=30)),
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
        ))
        db.send_create_signal(u'unicoresso', ['Repo'])

        # Adding M2M table for field users on 'Repo'
        m2m_table_name = db.shorten_name(u'unicoresso_repo_users')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('repo', models.ForeignKey(orm[u'unicoresso.repo'], null=False)),
            ('user', models.ForeignKey(orm[u'unicoresso.user'], null=False))
        ))
        db.create_unique(m2m_table_name, ['repo_id', 'user_id'])

        # Deleting model 'AuthorizedSite'
        db.delete_table(u'unicoresso_authorizedsite')

        # Removing M2M table for field group on 'AuthorizedSite'
        db.delete_table(db.shorten_name(u'unicoresso_authorizedsite_group'))


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
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'unicoresso.authorizedsite': {
            'Meta': {'object_name': 'AuthorizedSite'},
            'group': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Group']", 'symmetrical': 'False'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'site': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        }
    }

    complete_apps = ['unicoresso']