from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import Context, loader


def hod(request):
    try:
        assert request.session['name'][0:3]=='HOD'
        return HttpResponse('Welcome. Logged in as HOD id ='+request.session['name'])
    except AssertionError:
        return HttpResponse('Please re-login as HOD to gain access')
