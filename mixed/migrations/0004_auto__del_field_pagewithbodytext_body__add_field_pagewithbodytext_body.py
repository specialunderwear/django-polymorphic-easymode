# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Deleting field 'PageWithBodyText.body'
        db.delete_column('mixed_pagewithbodytext', 'body')

        # Adding field 'PageWithBodyText.body_en'
        db.add_column('mixed_pagewithbodytext', 'body_en', self.gf('django.db.models.fields.TextField')(null=True, blank=True), keep_default=False)

        # Adding field 'PageWithBodyText.body_nl'
        db.add_column('mixed_pagewithbodytext', 'body_nl', self.gf('django.db.models.fields.TextField')(null=True, blank=True), keep_default=False)


    def backwards(self, orm):
        
        # Adding field 'PageWithBodyText.body'
        db.add_column('mixed_pagewithbodytext', 'body', self.gf('django.db.models.fields.TextField')(default=u''), keep_default=False)

        # Deleting field 'PageWithBodyText.body_en'
        db.delete_column('mixed_pagewithbodytext', 'body_en')

        # Deleting field 'PageWithBodyText.body_nl'
        db.delete_column('mixed_pagewithbodytext', 'body_nl')


    models = {
        'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'mixed.owner': {
            'Meta': {'object_name': 'Owner'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        'mixed.pagebase': {
            'Meta': {'ordering': "('order',)", 'object_name': 'PageBase'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'meta_description': ('django.db.models.fields.TextField', [], {}),
            'order': ('django.db.models.fields.PositiveIntegerField', [], {'default': '99999999'}),
            'owner': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'pages'", 'to': "orm['mixed.Owner']"}),
            'polymorphic_ctype': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'polymorphic_mixed.pagebase_set'", 'null': 'True', 'to': "orm['contenttypes.ContentType']"}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '50', 'db_index': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        'mixed.pagewithbodytext': {
            'Meta': {'ordering': "('order',)", 'object_name': 'PageWithBodyText', '_ormbases': ['mixed.PageBase']},
            'body_en': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'body_nl': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'pagebase_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['mixed.PageBase']", 'unique': 'True', 'primary_key': 'True'})
        },
        'mixed.pagewithlink': {
            'Meta': {'ordering': "('order',)", 'object_name': 'PageWithLink', '_ormbases': ['mixed.PageBase']},
            'link': ('django.db.models.fields.URLField', [], {'max_length': '200'}),
            'pagebase_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['mixed.PageBase']", 'unique': 'True', 'primary_key': 'True'})
        }
    }

    complete_apps = ['mixed']
