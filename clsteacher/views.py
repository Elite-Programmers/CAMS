from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.template import Context, loader
from .models import FacEnr,ClassTchr,StudentSemEnr

def ctea(request):
    try:
        assert request.session['name'][0:3]=='CLT'
        return render_to_response('ctea.html')
    except AssertionError:
        return HttpResponse('Pleasse re-login as Class Teacher to gain access')

def faculty(request):
    try:
        assert request.session['name'][0:3]=='CLT'
    except AssertionError:
        return HttpResponse('Pleasse re-login as Class Teacher to gain access')
    rec1=ClassTchr.objects.get(fid__exact=request.session['name'][3:])
    sec=rec1.section
    yr=rec1.year
    rec2=FacEnr.objects.filter(section__exact=sec,year=yr)
    if rec2.count()>0:
        tmpl = loader.get_template("clt_faculty.html")
        cont = Context({'FacEnr': rec2})
        return HttpResponse(tmpl.render(cont))
    return HttpResponse('No Faculty enrolled for your section')

def student(request):
    try:
        assert request.session['name'][0:3]=='CLT'
    except AssertionError:
        return HttpResponse('Pleasse re-login as Class Teacher to gain access')
    rec1=ClassTchr.objects.get(fid__exact=request.session['name'][3:])
    sec=rec1.section
    yr=rec1.year
    rec2=StudentSemEnr.objects.filter(section__exact=sec,year=yr).order_by('batch')
    if rec2.count()>0:
        tmpl = loader.get_template("clt_student.html")
        cont = Context({'StudentSemEnr': rec2})
        return HttpResponse(tmpl.render(cont))
    return HttpResponse('No Student enrolled for your section')
