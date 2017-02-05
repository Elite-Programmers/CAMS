from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.template import Context, loader
from .forms import SemSecForm
from .models import FacEnr,StudentSemEnr

def facu(request):
    try:
        assert request.session['name'][0:3]=='FAC'
        return render_to_response('facu.html')
    except AssertionError:
        return HttpResponse('Please re-login as Faculty to gain access')

def student_data(request):
    try:
        assert request.session['name'][0:3]=='FAC'
    except AssertionError:
        return HttpResponse('Please re-login as Faculty to gain access')
    try:
        rec1=FacEnr.objects.get(fid__exact=request.session['name'][3:],year=yr,section=sec,scode__iregex=r'^.*'+(sem)+'[0-9]$')
    except FacEnr.DoesNotExist:
        return HttpResponse('You cannot avail the list which are not enrolled to you')
    rec2=StudentSemEnr.objects.filter(section=sec,year=yr,sem=sem)
    if rec2.count()>0:
        tmpl = loader.get_template("fac_student_data.html")
        cont = Context({'StudentSemEnr': rec2})
        return HttpResponse(tmpl.render(cont))
    return HttpResponse('No Faculty enrolled for the selected attributes')



def student(request):
    try:
        assert request.session['name'][0:3]=='FAC'
    except AssertionError:
        return HttpResponse('Please re-login as Faculty to gain access')
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
            return student_data(request)
    # if a GET (or any other method) we'll create a blank form
    else:
        form = SemSecForm()
    return render(request, 'fac_student.html', {'form': form})
