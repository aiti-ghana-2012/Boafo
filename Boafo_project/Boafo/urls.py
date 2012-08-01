from django.conf.urls.defaults import *

urlpatterns = patterns('',
    url(r'^$','Boafo.views.home'),
##    url(r'^services/$', 'Boafo.views.service_list'),
    url(r'^list/$', 'Boafo.views.category_list'),
    url(r'^/sms/$', 'Boafo.views.sms_request'),
    url(r'^category/(?P<id>\d+)/$', 'Boafo.views.servicecat_list'),
    url(r'^provider/(?P<id>\d+)/$', 'Boafo.views.provider_list'),
    url(r'^service/$', 'Boafo.views.service_list'),
    url(r'^about/$', 'Boafo.views.about'),
    url(r'^contact/$', 'Boafo.views.contact'),
    url(r'^mail/$', 'Boafo.views.mail'),
    url(r'^thanks/$', 'Boafo.views.thanks'),
    url(r'^register/$', 'Boafo.views.register'),
##    url(r'^service/(?P<id>\d+)/'),
##    url(r'^$', 'blog.views.home'),
##    url(r'^posts/$', 'blog.views.post_list'),
##    url(r'^comments/(?P<id>\d+)/\w+?$', 'blog.views.edit_comment'),
##    url(r'^posts/(?P<id>\d+)/((?P<showComments>.*)/)?$', 'blog.views.post_detail'),
   
    ## add your url here
##    url(r'^posts/search/(?P<text>\w+)/$','blog.views.post_search'),
)
