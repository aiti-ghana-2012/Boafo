# Create your views here.

from django.forms import ModelForm
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponseRedirect

from django.template import Context, loader
from django.shortcuts import render_to_response

from django.template import Context, loader
from django.http import HttpResponse

from dj_simple_sms.models import SMS

from models import *
######################################################################
######################################################################
########               SMS VIEWS FOR HANDLING OF CUSTOMER REQUESTS AND ERRORS         ############

## This one return the text which will be sent to the customer if a blank text is initially sent
def list_all_services():
    services = Service.objects.all()
    text ="All Services\n\n"
    for service in services:
        text = text + (str(service.pk) + " : " + service.service + "\n")
    text = text + "Please format your sms as: No. of service , Location\ne.g.  2, madina"
    return text

# This one returns the list of service providers with their contact details based on text sent by customer
def list_requested_sp(id,loc):
    s_pds = ServiceProvider.objects.filter(location = loc)
    text ="Av. Service-Providers\n\n"
    for sp in s_pds:
        text = text + ( sp.organization_name + "\n" + sp.personnel_name + str(sp.telephone) + "\n\n")
    text = text + "Thank you for using Boafo services."
    return text

# This one extracts the service no from the body of sent text
def extract_sno_from_text(body):
    service_no = str()
    for c in body:
        if(c !=' '):
            service_no = service_no + c
        else:
            return service_no
    return service_no

# This one extracts the location from the body of sent text
def extract_loc_from_text(body):
    location = str()
    for i in range((body.index(' ') +1),(len(body))):
        if(body[i].isalpha()):
            location = location + body[i]
    return location
    
######################################################################
######################################################################
#########                                                     SMS HANDLER                                                   ############

##  This view will handle sms requests
def sms_request(sms):
    dest = sms.to_number                    #incoming sms destination value/address
    customer = sms.from_number        # incoming sms source value/address
    body = sms.body                            # body of incoming text
    # if the text was sent to 'Boafo' or 'boafo'
    if (dest =='1430'):      #This can be changed to a shortcode we specify
        # if a blank text is sent initially sent
        if (body==''):
            text = list_all_services()  
            new_sms = SMS(to_number=customer, from_number=dest, body=text)
        else:
            text = "You entered " + body + ". \nThank you for using Boafo. "
##            no = int(extract_sno_from_text(body))
##            loc = extract_loc_from_text(body)
##            text = str(no) +" " + loc               # For now it just returns the text sent by the customer
##            text =  list_requested_sp(no,loc)
##            text = extract_sno_from_text(body) +" "+ extract_loc_from_text(body)
            # extract the two parts of the body
##            services = Service.objects.all()
##            text =str();
##        for service in services:
##            text = text + (str(service.pk) + " : " + service.service + "\n")
##        text = text + "\n\nPlease format your SMS as e.g. 2, Madina"
            new_sms = SMS(to_number=customer, from_number=dest, body=text)
    else:
        # if the text wasn't sent to Boafo/boafo, an sms is sent the customer
        new_sms = SMS(to_number=customer, from_number="Service Provider", body="Unknown Destination.\nUse 1430 for Boafo")
    new_sms.send()
    

    
######################################################################
######################################################################

##                  WEB     VIEWS     
##      Lists all categories
def category_list(request):
    categories =Category.objects.all()
    t = loader.get_template('Boafo/category_list.html')
    c = Context({'category':categories })
    return HttpResponse(t.render(c))

##  LIsts all available services
def service_list(request):
    services = Service.objects.all()
    t = loader.get_template('Boafo/service_list.html')
    c = Context({'services':services})
    return HttpResponse(t.render(c))

#  
#       Lists a particular category's details
def category_details(request,id):
    service = Service.objects.filter(category=id)
    #category=Category.objects.all()
    t = loader.get_template('Boafo/service.html')
    c = Context({'service':service})
    return HttpResponse(t.render(c))

# a l
def home(request):
    t = loader.get_template('Boafo/base.html')
    c = Context({ })
    return HttpResponse(t.render(c))
