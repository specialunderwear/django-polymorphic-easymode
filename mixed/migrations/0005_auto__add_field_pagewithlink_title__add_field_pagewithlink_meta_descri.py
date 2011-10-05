# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding field 'PageWithLink.title'
        db.add_column('mixed_pagewithlink', 'title', self.gf('django.db.models.fields.CharField')(default=u'title', max_length=255), keep_default=False)

        # Adding field 'PageWithLink.meta_description'
        db.add_column('mixed_pagewithlink', 'meta_description', self.gf('django.db.models.fields.TextField')(default=u'link'), keep_default=False)

        # Deleting field 'PageBase.meta_description'
        db.delete_column('mixed_pagebase', 'meta_description')

        # Deleting field 'PageBase.title'
        db.delete_column('mixed_pagebase', 'title')

        # Adding field 'PageWithBodyText.title_en'
        db.add_column('mixed_pagewithbodytext', 'title_en', self.gf('django.db.models.fields.CharField')(max_length=255, null=True), keep_default=False)

        # Adding field 'PageWithBodyText.title_nl'
        db.add_column('mixed_pagewithbodytext', 'title_nl', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True), keep_default=False)

        # Adding field 'PageWithBodyText.meta_description'
        db.add_column('mixed_pagewithbodytext', 'meta_description', self.gf('django.db.models.fields.TextField')(default=u'title'), keep_default=False)


    def backwards(self, orm):
        
        # Deleting field 'PageWithLink.title'
        db.delete_column('mixed_pagewithlink', 'title')

        # Deleting field 'PageWithLink.meta_description'
        db.delete_column('mixed_pagewithlink', 'meta_description')

        # Adding field 'PageBase.meta_description'
        db.add_column('mixed_pagebase', 'meta_description', self.gf('django.db.models.fields.TextField')(default=u'meta'), keep_default=False)

        # Adding field 'PageBase.title'
        db.add_column('mixed_pagebase', 'title', self.gf('django.db.models.fields.CharField')(default=u'title', max_length=255), keep_default=False)

        # Deleting field 'PageWithBodyText.title_en'
        db.delete_column('mixed_pagewithbodytext', 'title_en')

        # Deleting field 'PageWithBodyText.title_nl'
        db.delete_column('mixed_pagewithbodytext', 'title_nl')

        # Deleting field 'PageWithBodyText.meta_description'
        db.delete_column('mixed_pagewithbodytext', 'meta_description')


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
            'order': ('django.db.models.fields.PositiveIntegerField', [], {'default': '99999999'}),
            'owner': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'pages'", 'to': "orm['mixed.Owner']"}),
            'polymorphic_ctype': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'polymorphic_mixed.pagebase_set'", 'null': 'True', 'to': "orm['contenttypes.ContentType']"}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '50', 'db_index': 'True'})
        },
        'mixed.pagewithbodytext': {
            'Meta': {'ordering': "('order',)", 'object_name': 'PageWithBodyText', '_ormbases': ['mixed.PageBase']},
            'body_en': ('django.db.models.fields.TextField', [], {'null': 'True'}),
            'body_nl': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'meta_description': ('django.db.models.fields.TextField', [], {}),
            'pagebase_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['mixed.PageBase']", 'unique': 'True', 'primary_key': 'True'}),
            'title_en': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True'}),
            'title_nl': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'})
        },
        'mixed.pagewithlink': {
            'Meta': {'ordering': "('order',)", 'object_name': 'PageWithLink', '_ormbases': ['mixed.PageBase']},
            'link': ('django.db.models.fields.URLField', [], {'max_length': '200'}),
            'meta_description': ('django.db.models.fields.TextField', [], {}),
            'pagebase_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['mixed.PageBase']", 'unique': 'True', 'primary_key': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        }
    }

    complete_apps = ['mixed']
