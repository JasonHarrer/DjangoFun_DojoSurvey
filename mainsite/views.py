from django.shortcuts import render, redirect
from django.http import HttpResponseNotAllowed
from . import data

# Create your views here.

def index(request):
    context = { 
                "locations": data.locations, 
                "languages": data.languages
              }
    return render(request, "index.html", context)


def process_dojo_survey(request):
    if request.method != 'POST':
        return HttpResponseNotAllowed(['POST'], 'Error: This page is only used to process form results.  Calling it directly via a GET request is not allowed.') 
    request.session['name']      = request.POST['name']
    request.session['location']  = request.POST['location']
    request.session['languages'] = request.POST.getlist('languages')
    request.session['comments']  =  request.POST['comments']
    if request.session['comments'] == '':
        request.session['comments'] = None
    return redirect('/result')


def result(request):
    return render(request, "result.html")
