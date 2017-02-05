from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import Context, loader
from .models import FacultyList,ClassTchr
from .forms import SemSecForm

def auth(request):
    try:
        assert request.session['name'][0:3]=='HOD'
        return HttpResponse('Welcome. Logged in as HOD id ='+request.session['name'])
    except AssertionError:
        return HttpResponse('Please re-login as HOD to gain access')

def hoda(request):
    hrec=FacultyList.objects.get(fid__exact=request.session['name'][3:])
    dept=hrec.branch
    rec2=FacultyList.objects.filter(branch__exact=dept).values_list('fid', flat=True)
    rec=ClassTchr.objects.filter(fid__in=rec2)
    tmpl = loader.get_template("ct.html")
    cont = Context({'ClassTchr': rec})
    return HttpResponse(tmpl.render(cont))


def hod(request):
    try:
        assert request.session['name'][0:3]=='HOD'
        return render_to_response('hod.html')

    except AssertionError:
        return HttpResponse('Please re-login as HOD to gain access')

def cltchr_data(request):
    try:
        assert request.session['name'][0:3]=='HOD'
    except AssertionError:
        return HttpResponse('Please re-login as HOD to gain access')
    rec1=FacultyList.objects.get(fid__exact=request.session['name'][3:])
    bran=rec1.branch
    rec2=FacultyList.objects.filter(branch__exact=bran).values_list('fid')
    if sem=='ALL' and sec=='ALL':
        rec3=ClassTchr.objects.filter(fid__in=rec2,year=yr)
    elif sem=='ALL':
        rec3=ClassTchr.objects.filter(fid__in=rec2,year=yr,section=sec)
    elif sec=='ALL':
        rec3=ClassTchr.objects.filter(fid__in=rec2,year=yr,sem=sem)
    else:
        rec3=ClassTchr.objects.filter(fid__in=rec2,year=yr,sem=sem,section=sec)
    if rec3.count()>0:
        tmpl = loader.get_template("cltchr.html")
        cont = Context({'ClassTchr': rec3})
        return HttpResponse(tmpl.render(cont))
    return HttpResponse('No ClassTeachers for the selected attributes')




def cltchr(request):
    try:
        assert request.session['name'][0:3]=='HOD'
    except AssertionError:
        return HttpResponse('Please re-login as HOD to gain access')
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = SemSecForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            global sem,sec,yr
            sec=form.cleaned_data.get('section')
            sem=form.cleaned_data.get('semester')
            yr=form.cleaned_data.get('year')
            return cltchr_data(request)
    # if a GET (or any other method) we'll create a blank form
    else:
        form = SemSecForm()
    return render(request, 'hod_cltchr.html', {'form': form})
