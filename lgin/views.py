from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response
from .forms import LoginForm
from django.template import Context, loader
from .models import CamsLogin, FacultyList, ClassTchr

uid=None

def admn(request):
    rec=CamsLogin.objects.all()
    tmpl = loader.get_template("admn.html")
    cont = Context({'CamsLogin': rec})
    return HttpResponse(tmpl.render(cont))

def lerror(request):
    return HttpResponse('Invalid Username/Password Entered')

def decrole(request):
    try:
        rec = FacultyList.objects.get(fid__exact=uid,designation__contains='HOD')
        request.session['name']='HOD'+uid
        return HttpResponseRedirect('/login/hod/')
    except FacultyList.DoesNotExist:
        try:
            rec = ClassTchr.objects.get(fid__exact=uid)
            request.session['name']='CLT'+uid
            return HttpResponseRedirect('/login/clsteacher/')
        except ClassTchr.DoesNotExist:
            try:
                rec = FacultyList.objects.get(fid__exact=uid)
                request.session['name']='FAC'+uid
                return HttpResponseRedirect('/login/faculty/')
            except FacultyList.DoesNotExist:
                request.session['name']='STU'+uid
                return HttpResponseRedirect('/login/student/')

def login(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = LoginForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            global uid
            uid=form.cleaned_data.get('usr')
            p=form.cleaned_data.get('pwd')
            try:
                rec = CamsLogin.objects.get(userid__iexact=uid,password__exact=p)
                request.session.set_expiry(0)
                uid=rec.userid
                # redirect to a new URL:
                return decrole(request)
            except CamsLogin.DoesNotExist:
                return lerror(request)
    # if a GET (or any other method) we'll create a blank form
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})
