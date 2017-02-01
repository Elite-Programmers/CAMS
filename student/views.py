from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import Context, loader

def student(request):
    try:
        assert request.session['name'][0:3]=='STU'
        return HttpResponse('Welcome. Logged in as Student id ='+request.session['name'])
    except AssertionError:
        return HttpResponse('Please re-login as Student to gain access')
