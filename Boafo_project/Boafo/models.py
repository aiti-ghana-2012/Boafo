from django.db import models

# Create your models here.
## CREATING MODELS FOR BOAFO SERVICE

##class Comment(models.Model):
##        body = models.TextField()
##        author = models.CharField(max_length =60)
##        created = models.DateField(auto_now_add = True)
##        updated = models.DateField(auto_now =True)
##        post = models.ForeignKey(Post)
##        def fscb(self):
##            return self.body[:60]

#       The Location Model with only one visible field, Location
class Location(models.Model):
    location = models.CharField(max_length = 255)

#       The ServiceProvider Model
class ServiceProvider(models.Model):
    organization_name = models.CharField(max_length = 255)
    personnel_name = models.CharField(max_length = 255)
    telephone = models.
    email = 
    service = models.ForeignKey(Service):
    location = models.ForeignKey(Location)
