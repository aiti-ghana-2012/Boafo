# Create your views here.

from django.forms import ModelForm
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponseRedirect

from django.template import Context, loader
from django.shortcuts import render_to_response

from django.template import Context, loader
from django.http import HttpResponse

from models import Service, Category


def category_list(request):
    #service = Service.objects.all()
    category=Category.objects.all()
    t = loader.get_template('Boafo/category_list.html')
    c = Context({'category':category })
    return HttpResponse(t.render(c))


def service_list(request,id):
    service = Service.objects.filter(category=id)
    #category=Category.objects.all()
    t = loader.get_template('Boafo/service_list.html')
    c = Context({'service':service})
    return HttpResponse(t.render(c))

def home(request):
    t = loader.get_template('Boafo/base.html')
    c = Context({ })
    return HttpResponse(t.render(c))
