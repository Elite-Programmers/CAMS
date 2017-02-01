from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import Context, loader

def facu(request):
    try:
        assert request.session['name'][0:3]=='FAC'
        return HttpResponse('Welcome. Logged in as Faculty id ='+request.session['name'])
    except AssertionError:
        return HttpResponse('Please re-login as Faculty to gain access')
