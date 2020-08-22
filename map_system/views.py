from django.shortcuts import render, redirect , HttpResponse
import os
from .models import *

# Create your views here.

def map_dashboard(request):
        context = {
        "map_api" : os.environ.get('GMAP_APIKEY')   
        }
        return render (request, 'map_main.html', context)

