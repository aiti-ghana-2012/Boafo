from django.conf.urls import patterns, include, url
from Boafo.views import *
import views

urlpatterns = patterns('',
    url(r'^$', views.sms),
    url(r'^sms/$',sms_request)
)
