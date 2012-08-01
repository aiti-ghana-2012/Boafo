# Create your views here.
import re
from django.forms import ModelForm
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponseRedirect
from django.shortcuts import render
#from django.http import HttpResponseRedirect
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
    text = text + "Please format your sms as: service_no location\ne.g.  2 madina"
    return text

# This one returns the list of service providers with their contact details based on text sent by customer
def list_requested_sp(id,loc):
    loc_no = Location.objects.get(location = loc)
    s_pds = ServiceProvider.objects.filter(location = loc_no.pk).filter(service=id)
    if(s_pds.exists()):
        text ="Av. Service-Providers\n\n"
        for sp in s_pds:
            text = text + ( "SP      : " + sp.organization_name + "\n" + "Contact : "+ sp.personnel_name+ "\n" + str(sp.telephone) + "\n\n")
        text = text + "Thank you for using Boafo services."
    else:
        text = "Your search returned no results. Please try again in a few minutes."
    return text

#  This one checks the text for correct formatting
def check_text(body):
    match = re.match(r'^\d+\s+\w+$',body)
    wordmatch = re.match(r'^\w+\s+\w+$',body)
    if match:
        return 1
    elif wordmatch:
        return 2
    else:
        return False


# This composes a help text for the customer
def help_text(body):
    text = "Input error: " + body +" does not match our format.\n Send blank sms or 'help' to 1430 for assistance."
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

## This view extracts the service from the text and returns the service no
def extract_srv_from_text(body):
    service = str()
    for c in body:
        if (c.)

# This one extracts the location from the body of sent text
def extract_loc_from_text(body):
    location = str()
    for i in range((body.index(' ') +1),(len(body))):
        if(body[i].isalpha()):
            location = location + body[i]
    return location.strip().lower()                  # strip any whitespace and convert to lowercase before rendering location
    
######################################################################
######################################################################
#########                                                     SMS HANDLER                                                   ############

##  This view will handle sms requests
def sms_request(sms):
    dest = sms.to_number                    #incoming sms destination value/address
    customer = sms.from_number        # incoming sms source value/address
    body = sms.body                            # body of incoming text
    # if the text was sent to 'Boafo' or 'boafo'

    if (body=='' or body =='help'):
        text = list_all_services()  
        new_sms = SMS(to_number=customer, from_number=dest, body=text)
    else:
        if (check_text(body) == 1):                                     # check text for correct format
            sno = int(extract_sno_from_text(body))     # extract service no from body
            location = extract_loc_from_text(body)      # extract location from body
        elif (check_text(body) == 2):
            location = extract_loc_from_text(body)      # extract location from body
            sno = extract_srv_from_text(body)
        text = list_requested_sp(sno,location)        # all services providers matching the criteria are stored
        else:
            text = help_text(body)                               # a help text is sent to the customer
        new_sms = SMS(to_number=customer, from_number=dest, body=text)
    new_sms.send()
    

 #####################              END OF SMS HANDLER                 #######################   
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


##  LIsts all available services for a category
def servicecat_list(request,id):
    services_cat = Service.objects.filter(category=id)
    t = loader.get_template('Boafo/service_list.html')
    c = Context({'services':services_cat})
    return HttpResponse(t.render(c))

##  LIsts all available serviceproviders for a specific service
def provider_list(request,id):
    service = Service.objects.get(pk=id)
    provider = ServiceProvider.objects.filter(service=id)
    t = loader.get_template('Boafo/serviceprovider.html')
    c = Context({'service':service,'provider':provider})
    return HttpResponse(t.render(c))


#  
#       Lists a particular category's details
def category_details(request,id):
    service = Service.objects.extra(where=["pk=%d"], params=[id])
    #category=Category.objects.all()
    t = loader.get_template('Boafo/service.html')
    c = Context({'service':service})
    return HttpResponse(t.render(c))


#def do_search(request):
#    if request.method == 'POST': # If the form has been submitted...
#        form = SearchForm(request.POST) # A form bound to the POST data
#        if form.is_valid(): # All validation rules pass
#            # Process the data in form.cleaned_data
#            # ...
#            return HttpResponseRedirect('//') # Redirect after POST
#    else:
#        form = SearchtForm() # An unbound form#

#    return render(request, 'contact.html', {'form': form,})



# a l
def home(request):
    t = loader.get_template('Boafo/base.html')
    c = Context({ })
    return HttpResponse(t.render(c))

# This is the about boafo page
def about(request):
    t = loader.get_template('Boafo/about.html')
    c = Context({ })
    return HttpResponse(t.render(c))


# This is the contact boafo page
def contact(request):
    t = loader.get_template('Boafo/feedback_form.html')
    c = Context({ })
    return HttpResponse(t.render(c))

@csrf_exempt
# This is the Mail boafo page
def mail(request):
    t = loader.get_template('Boafo/send_mail.php')
    c = Context({ })
    return HttpResponse(t.render(c))

@csrf_exempt
# This is the Thank You page
def thanks(request):
    t = loader.get_template('Boafo/thankyou.html')
    c = Context({ })
    return HttpResponse(t.render(c))
