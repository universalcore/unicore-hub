# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'User'
        db.create_table(u'unicoresso_user', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('username', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('password', self.gf('django.db.models.fields.CharField')(max_length=30)),
        ))
        db.send_create_signal(u'unicoresso', ['User'])

        # Adding model 'Repo'
        db.create_table(u'unicoresso_repo', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('url', self.gf('django.db.models.fields.CharField')(max_length=30)),
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


    def backwards(self, orm):
        # Deleting model 'User'
        db.delete_table(u'unicoresso_user')

        # Deleting model 'Repo'
        db.delete_table(u'unicoresso_repo')

        # Removing M2M table for field users on 'Repo'
        db.delete_table(db.shorten_name(u'unicoresso_repo_users'))


    models = {
        u'unicoresso.repo': {
            'Meta': {'object_name': 'Repo'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'url': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'users': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['unicoresso.User']", 'symmetrical': 'False'})
        },
        u'unicoresso.user': {
            'Meta': {'object_name': 'User'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'username': ('django.db.models.fields.CharField', [], {'max_length': '30'})
        }
    }

    complete_apps = ['unicoresso']