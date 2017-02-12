from django import forms
from .models import FacEnr,StudentSemEnr,StudentList
import datetime

SEM = (
    ('ALL', 'ALL'),
    ('1', 'Sem 1'),
    ('2', 'Sem 2'),
    ('3', 'Sem 3'),
    ('4', 'Sem 4'),
    ('5', 'Sem 5'),
    ('6', 'Sem 6'),
    ('7', 'Sem 7'),
    ('8', 'Sem 8'),
)
SECTION = (
    ('ALL','ALL'),
    ('A','A'),
    ('B','B'),
    ('C','C'),
    ('D','D'),
    ('E','E'),
)

SEM2 = (
    ('1', 'Sem 1'),
    ('2', 'Sem 2'),
    ('3', 'Sem 3'),
    ('4', 'Sem 4'),
    ('5', 'Sem 5'),
    ('6', 'Sem 6'),
    ('7', 'Sem 7'),
    ('8', 'Sem 8'),
)
SECTION2 = (
    ('A','A'),
    ('B','B'),
    ('C','C'),
    ('D','D'),
    ('E','E'),
)
SLOTS = (
    ('1', ' 1'),
    ('2', ' 2'),
    ('3', ' 3'),
    ('4', ' 4'),
    ('5', ' 5'),
    ('6', ' 6'),
    ('7', ' 7'),
)


class SemSecForm(forms.Form):
    semester = forms.ChoiceField(label='Select Semester', choices=SEM)
    section = forms.ChoiceField(label='Select Section',choices=SECTION)
    year = forms.IntegerField(initial=2017,min_value=2017,max_value=2100)

class AttForm(forms.Form):
    semester = forms.ChoiceField(label='Select Semester', choices=SEM2)
    section = forms.ChoiceField(label='Select Section',choices=SECTION2)


class Att2Form(forms.Form):
    slot = forms.ChoiceField(choices = SLOTS)
    def __init__(self,*args,**kwargs):
        mySection = kwargs.pop("section")
        mySem = kwargs.pop("semester")
        myFid = kwargs.pop("faculty")
         # client is the parameter passed from views.py
        super(Att2Form, self).__init__(*args,**kwargs)
        self.fields['sub'] = forms.ChoiceField(label='Subject Code',choices=[(x.scode, x.scode) for x in FacEnr.objects.filter(fid=myFid,year=datetime.date.today().year,section=mySection)])
        rec=StudentSemEnr.objects.filter(branch='CS',section=mySection,sem=mySem).values_list('usn')
        self.fields['ids'] =forms.MultipleChoiceField(label='Student List',widget=forms.CheckboxSelectMultiple(attrs={"checked":""}), choices=[(x.usn.userid, x.usn.userid+': '+x.sname) for x in StudentList.objects.filter(usn__in=rec)])
