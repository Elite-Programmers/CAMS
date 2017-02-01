from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import Context, loader

def ctea(request):
    try:
        assert request.session['name'][0:3]=='CLT'
        return HttpResponse('Welcome. Logged in as Class Teacher id ='+request.session['name'])
    except AssertionError:
        return HttpResponse('Pleasse re-login as Class Teacher to gain access')
