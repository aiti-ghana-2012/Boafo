from django.db import models

# Create your models here.

#       CREATING THE MODEL Location

class Location (models.Model):
    location = models.CharField(max_length = 255)               # various locations in the system. service providers
                                                                                             # will choose a location from a drop down menu

#       CREATING THE MODEL ServiceProvider
class ServiceProvider(models.Model):
    organization_name = models.CharField(max_length = 255)  #organisational name of service provider
    personnel_name = models.CharField(max_length = 255)     #name of personnel at organisation
    telephone  = models.CharField(max_length =  20)               # service provider's telephone
    email = models.EmailField()                                                  # service provider's email
    service = models.ForeignKey(Location)                                # kind of service provided by service provider
    location = models.ForeignKey(Location)                               # service provider's location

#       CREATING THE MODEL Service
class Service(models.Model):                                                    
    service = models.CharField(max_length = 255)                   # The name of the service
    category = models.ForeignKey(Category)                            # this maps a service to a category 

#       CREATING THE MODEL Category
class Category (models.Model):
    service_category = models.CharField(max_length = 255)    # 
    description = models.TextField()

#       CREATING THE MODEL Subscription
class Subscription (models.Model):
    amount = models.FloatField()
    subscription_date = models.DateField(auto_now_add = True) # date for subscription
    subscription_tracker = models.BooleanField()                        # to check whether a service provider has subscribed or not
    count = models.IntegerField()                                               #  keeps track of the number of times a service provider's
                                                                                                # details are sent to a customer
    organization = models.ForeignKey(ServiceProvider)             # the subscription detail is linked to the service provider on the
                                                                                                # primary key of the service provider
    
