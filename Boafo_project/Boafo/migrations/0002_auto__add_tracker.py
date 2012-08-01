# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'Tracker'
        db.create_table('Boafo_tracker', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('date', self.gf('django.db.models.fields.DateField')(auto_now_add=True, blank=True)),
            ('total_request_count', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('total_requests_full', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('total_requests_fail', self.gf('django.db.models.fields.IntegerField')(default=0)),
        ))
        db.send_create_signal('Boafo', ['Tracker'])


    def backwards(self, orm):
        
        # Deleting model 'Tracker'
        db.delete_table('Boafo_tracker')


    models = {
        'Boafo.category': {
            'Meta': {'object_name': 'Category'},
            'description': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'service_category': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        'Boafo.location': {
            'Meta': {'object_name': 'Location'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'location': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        'Boafo.service': {
            'Meta': {'object_name': 'Service'},
            'category': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['Boafo.Category']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'service': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        'Boafo.serviceprovider': {
            'Meta': {'object_name': 'ServiceProvider'},
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'location': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['Boafo.Location']"}),
            'organization_name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'personnel_name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'service': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['Boafo.Service']", 'symmetrical': 'False'}),
            'telephone': ('django.db.models.fields.CharField', [], {'max_length': '20'})
        },
        'Boafo.subscription': {
            'Meta': {'object_name': 'Subscription'},
            'amount': ('django.db.models.fields.FloatField', [], {}),
            'count': ('django.db.models.fields.IntegerField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'organization': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['Boafo.ServiceProvider']"}),
            'subscription_date': ('django.db.models.fields.DateField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'subscription_tracker': ('django.db.models.fields.BooleanField', [], {'default': 'False'})
        },
        'Boafo.tracker': {
            'Meta': {'object_name': 'Tracker'},
            'date': ('django.db.models.fields.DateField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'total_request_count': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'total_requests_fail': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'total_requests_full': ('django.db.models.fields.IntegerField', [], {'default': '0'})
        }
    }

    complete_apps = ['Boafo']
