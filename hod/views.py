from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import Context, loader
from .models import FacultyList,ClassTchr

def ohod(request):
    try:
        assert request.session['name'][0:3]=='HOD'
        return HttpResponse('Welcome. Logged in as HOD id ='+request.session['name'])
    except AssertionError:
        return HttpResponse('Please re-login as HOD to gain access')

def hod(request):
    hrec=FacultyList.objects.get(fid__exact=request.session['name'][3:])
    dept=hrec.branch
    rec2=FacultyList.objects.filter(branch__exact=dept).values_list('fid', flat=True)
    rec=ClassTchr.objects.filter(fid__in=rec2)
    tmpl = loader.get_template("ct.html")
    cont = Context({'ClassTchr': rec})
    return HttpResponse(tmpl.render(cont))
