from django.db import models
from django.contrib import admin
# Create your models here.

#       CREATING THE MODEL Location

class Location (models.Model):
    location = models.CharField(max_length = 255)               # various locations in the system. service providers
                                                                                             # will choose a location from a drop down menu
    def __unicode__(self):
        return self.location

#       CREATING THE MODEL Category
class Category (models.Model):
    service_category = models.CharField(max_length = 255)    # 
    description = models.TextField()
    def __unicode__(self):
        return self.service_category


#       CREATING THE MODEL Service
class Service(models.Model):                                                    
    service = models.CharField(max_length = 255)                   # The name of the service
    category = models.ForeignKey(Category)                            # this maps a service to a category
    def __unicode__(self):
        return self.service

#       CREATING THE MODEL ServiceProvider
class ServiceProvider(models.Model):
    organization_name = models.CharField(max_length = 255)  #organisational name of service provider
    personnel_name = models.CharField(max_length = 255)     #name of personnel at organisation
    telephone  = models.CharField(max_length =  20)               # service provider's telephone
    email = models.EmailField()                                                  # service provider's email
    service = models.ForeignKey(Service)                                # kind of service provided by service provider
    location = models.ForeignKey(Location)                               # service provider's location
    def __unicode__(self):
        return self.organization_name


#       CREATING THE MODEL Subscription
class Subscription (models.Model):
    amount = models.FloatField()
    subscription_date = models.DateField(auto_now_add = True) # date for subscription
    subscription_tracker = models.BooleanField()                        # to check whether a service provider has subscribed or not
    count = models.IntegerField()                                               #  keeps track of the number of times a service provider's
                                                                                                # details are sent to a customer
    organization = models.ForeignKey(ServiceProvider)             # the subscription detail is linked to the service provider on the
                                                                                                # primary key of the service provider
    def __unicode__(self):
        return self.subscription_tracker


##class CommentInline(admin.TabularInline):
##        model = Comment
##
##class PostAdmin(admin.ModelAdmin):
##        list_display = ('title','created','updated')
##        search_param = ('title','body')
##        list_filter=('created','author')
##        inlines = [CommentInline]
##	
##	
##class CommentAdmin(admin.ModelAdmin):
##        list_display = ('post','author','fscb','created','updated')
##        search_param = ('created','author')
##admin.site.register(Post, PostAdmin)
##admin.site.register(Comment, CommentAdmin)
    
admin.site.register(Location)
admin.site.register(ServiceProvider)
admin.site.register(Service)
admin.site.register(Category)
admin.site.register(Subscription)
