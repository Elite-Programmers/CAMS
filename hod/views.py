import datetime
from django.db import IntegrityError
from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render_to_response,redirect
from django.template import Context, loader
from .models import FacultyList,ClassTchr,FacEnr,StudentSemEnr,CamsLogin,StudentList,Att
from .forms import SemSecForm,AttForm,Att2Form
global sem,sec
sem=1
sec='B'
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


def faculty_data(request):
    try:
        assert request.session['name'][0:3]=='HOD'
    except AssertionError:
        return HttpResponse('Please re-login as HOD to gain access')
    rec1=FacultyList.objects.get(fid__exact=request.session['name'][3:])
    bran=rec1.branch
    if sem=='ALL' and sec=='ALL':
        rec2=FacEnr.objects.filter(branch__exact=bran,year=yr).order_by('scode','section','slot')
    elif sem=='ALL':
        rec2=FacEnr.objects.filter(branch__exact=bran,year=yr,section=sec)
    elif sec=='ALL':
        rec2=FacEnr.objects.filter(branch__exact=bran,year=yr,scode__iregex=r'^.*'+(sem)+'[0-9]$').order_by('slot')
    else:
        rec2=FacEnr.objects.filter(branch__exact=bran,year=yr,scode__iregex=r'^.*'+(sem)+'[0-9]$',section=sec).order_by('day','slot')
    if rec2.count()>0:
        tmpl = loader.get_template("faculty.html")
        cont = Context({'FacEnr': rec2})
        return HttpResponse(tmpl.render(cont))
    return HttpResponse('No Faculty enrolled for the selected attributes')


def faculty(request):
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
            return faculty_data(request)
    # if a GET (or any other method) we'll create a blank form
    else:
        form = SemSecForm()
    return render(request, 'hod_faculty.html', {'form': form})


def student_data(request):
    try:
        assert request.session['name'][0:3]=='HOD'
    except AssertionError:
        return HttpResponse('Please re-login as HOD to gain access')
    rec1=FacultyList.objects.get(fid__exact=request.session['name'][3:])
    bran=rec1.branch
    if sem=='ALL' and sec=='ALL':
        rec2=StudentSemEnr.objects.filter(branch=bran,year=yr)
    elif sem=='ALL':
        rec2=StudentSemEnr.objects.filter(branch=bran,year=yr,section=sec)
    elif sec=='ALL':
        rec2=StudentSemEnr.objects.filter(branch=bran,year=yr,sem=sem)
    else:
        rec2=StudentSemEnr.objects.filter(branch=bran,year=yr,sem=sem,section=sec)
    if rec2.count()>0:
        tmpl = loader.get_template("student.html")
        cont = Context({'StudentSemEnr': rec2})
        return HttpResponse(tmpl.render(cont))
    return HttpResponse('No Students enrolled for the selected attributes')




def student(request):
    try:
        assert request.session['name'][0:3]=='HOD'
    except AssertionError:
        return HttpResponse('Please re-login as HOD to gain access')
    global sem,sec,yr
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = SemSecForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            sec=form.cleaned_data.get('section')
            sem=form.cleaned_data.get('semester')
            yr=form.cleaned_data.get('year')
            return student_data(request)
    # if a GET (or any other method) we'll create a blank form
    else:
        form = SemSecForm()
    return render(request, 'hod_student.html', {'form': form})

def student_list(request):
    try:
        assert request.session['name'][0:3]=='HOD'
    except AssertionError:
        return HttpResponse('Please re-login as HOD to gain access')
    global sem,sec
    form = Att2Form(semester=sem,section=sec,faculty=request.session['name'][3:])
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = Att2Form(request.POST,semester=sem,section=sec,faculty=request.session['name'][3:])
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            subject=form.cleaned_data.get('sub')
            usns=form.cleaned_data.get('ids')
            myslot=form.cleaned_data.get('slot')
            rec=CamsLogin.objects.all()
            rec2=StudentSemEnr.objects.filter(branch='CS',section=sec,sem=sem)
            for x in rec:
                if x.userid in usns:
                    bb=StudentList.objects.get(usn=x.userid)
                    db=Att.objects.create(usn=bb,slot=myslot,year=datetime.date.today(),scode=subject,poa='P')

                else:
                    for y in rec2:
                        if y.usn.usn.userid==x.userid:
                            bb=StudentList.objects.get(usn=x.userid)
                            db=Att.objects.create(usn=bb,slot=myslot,year=datetime.date.today(),scode=subject,poa='A')




            return HttpResponse("Successful")

    #This fills up the "choices"

    # if a GET (or any other method) we'll create a blank form

    return render(request, 'hod_att2.html', {'form': form})


def attn(request):
    try:
        assert request.session['name'][0:3]=='HOD'
    except AssertionError:
        return HttpResponse('Please re-login as HOD to gain access')
    global sem,sec
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = AttForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            sec=form.cleaned_data.get('section')
            sem=form.cleaned_data.get('semester')
            return redirect('/login/hod/att2/')
    # if a GET (or any other method) we'll create a blank form
    else:
        form = AttForm()
    return render(request, 'hod_att.html', {'form': form})
