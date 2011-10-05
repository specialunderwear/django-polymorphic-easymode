# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'Owner'
        db.create_table('mixed_owner', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=255)),
        ))
        db.send_create_signal('mixed', ['Owner'])

        # Adding field 'PageBase.owner'
        db.add_column('mixed_pagebase', 'owner', self.gf('django.db.models.fields.related.ForeignKey')(default=1, related_name='pages', to=orm['mixed.Owner']), keep_default=False)


    def backwards(self, orm):
        
        # Deleting model 'Owner'
        db.delete_table('mixed_owner')

        # Deleting field 'PageBase.owner'
        db.delete_column('mixed_pagebase', 'owner_id')


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
            'body': ('django.db.models.fields.TextField', [], {}),
            'pagebase_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['mixed.PageBase']", 'unique': 'True', 'primary_key': 'True'})
        },
        'mixed.pagewithlink': {
            'Meta': {'ordering': "('order',)", 'object_name': 'PageWithLink', '_ormbases': ['mixed.PageBase']},
            'link': ('django.db.models.fields.URLField', [], {'max_length': '200'}),
            'pagebase_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['mixed.PageBase']", 'unique': 'True', 'primary_key': 'True'})
        }
    }

    complete_apps = ['mixed']
