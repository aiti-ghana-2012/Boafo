# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'Location'
        db.create_table('Boafo_location', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('location', self.gf('django.db.models.fields.CharField')(max_length=255)),
        ))
        db.send_create_signal('Boafo', ['Location'])

        # Adding model 'Category'
        db.create_table('Boafo_category', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('service_category', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('description', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal('Boafo', ['Category'])

        # Adding model 'Service'
        db.create_table('Boafo_service', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('service', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('category', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['Boafo.Category'])),
        ))
        db.send_create_signal('Boafo', ['Service'])

        # Adding model 'ServiceProvider'
        db.create_table('Boafo_serviceprovider', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('organization_name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('personnel_name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('telephone', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('email', self.gf('django.db.models.fields.EmailField')(max_length=75)),
            ('location', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['Boafo.Location'])),
        ))
        db.send_create_signal('Boafo', ['ServiceProvider'])

        # Adding M2M table for field service on 'ServiceProvider'
        db.create_table('Boafo_serviceprovider_service', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('serviceprovider', models.ForeignKey(orm['Boafo.serviceprovider'], null=False)),
            ('service', models.ForeignKey(orm['Boafo.service'], null=False))
        ))
        db.create_unique('Boafo_serviceprovider_service', ['serviceprovider_id', 'service_id'])

        # Adding model 'Subscription'
        db.create_table('Boafo_subscription', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('amount', self.gf('django.db.models.fields.FloatField')()),
            ('subscription_date', self.gf('django.db.models.fields.DateField')(auto_now_add=True, blank=True)),
            ('subscription_tracker', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('count', self.gf('django.db.models.fields.IntegerField')()),
            ('organization', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['Boafo.ServiceProvider'])),
        ))
        db.send_create_signal('Boafo', ['Subscription'])


    def backwards(self, orm):
        
        # Deleting model 'Location'
        db.delete_table('Boafo_location')

        # Deleting model 'Category'
        db.delete_table('Boafo_category')

        # Deleting model 'Service'
        db.delete_table('Boafo_service')

        # Deleting model 'ServiceProvider'
        db.delete_table('Boafo_serviceprovider')

        # Removing M2M table for field service on 'ServiceProvider'
        db.delete_table('Boafo_serviceprovider_service')

        # Deleting model 'Subscription'
        db.delete_table('Boafo_subscription')


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
        }
    }

    complete_apps = ['Boafo']
