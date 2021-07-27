from django.shortcuts import render
from django.http import HttpResponseNotAllowed
from . import data

# Create your views here.

def index(request):
    context = { 
                "locations": data.locations, 
                "languages": data.languages
              }
    return render(request, "index.html", context)

def result(request):
    if request.method != 'POST':
        return HttpResponseNotAllowed(['POST'], 'Error: This page is only used to process form results.  Calling it directly via a GET request is not allowed.') 
    context = {
                'name':      request.POST['name'],
                'location':  request.POST['location'],
                'languages': request.POST.getlist('languages'),
                'comments':  request.POST['comments']
              }
    if context['comments'] == '':
        context['comments'] = None
    return render(request, "result.html", context)
