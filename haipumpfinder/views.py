from django.shortcuts import get_object_or_404, render, HttpResponse, Http404
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponseRedirect
from django.template import Context, Template 
from django.urls import reverse
from django.views import generic
#import pdb; pdb.set_trace()
from .services import Trial, TrialLocation
from .models import Hospital 



def trial(request,trial_id):
    t = Trial(trial_id) 
    print("Trial Name: " + t.name)
    page_title = "Trial Finder- Finds clinics offering the " + t.name
    #print("Trial URL :" + t.CTGovURL)
    try:
        sites_list = t.locations 
    except:
        raise Http404("Trial ID not found") 

    sites_dict = {
        'sites_list': sites_list,
        'trial_name': t.name,
        'trial_id': trial_id,
        'page_title': page_title,
    }
    return render(request,'haipumpfinder/trial.html', sites_dict)

# console.log('Got here bitch!')
#sites_list = Trial.locations('NCT02928224')
#print("Sites Count: " + sites_list[0].city)
#return HttpResponse("Got test to Trial!")
#return render(request,'trial.html',sites_list) 





class IndexView(generic.ListView):
    page_title = "HAI Pump Finder- Finds clinics offering the HAI Pump"
    template_name = 'haipumpfinder/index.html'
    context_object_name = 'hospital_list'
    #print(Hospital.objects.count())
    def get_queryset(self):
        """Return all published hospitals."""
        return Hospital.objects.order_by('id')


class DetailView(generic.DetailView):
    model = Hospital
    template_name = 'haipumpfinder/detail.html'



class ResultsView(generic.DetailView):
    template_name = 'haipumpfinder/what-the-hai.html'

class ResultsView(generic.DetailView):
    template_name = 'haipumpfinder/news.html'

#class Address_List(Hospitals)
#     @property
#    def get_address(self):
#        address_list = []  
#        for hospital in Hospital.objects.all()
#          address_list = address_list.append[hospital.city]  
#        endfor 
#        return address_list