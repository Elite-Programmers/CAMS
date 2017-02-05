from django import forms

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

class SemSecForm(forms.Form):
    semester = forms.ChoiceField(label='Select Semester', choices=SEM)
    section = forms.ChoiceField(label='Select Section',choices=SECTION)
    year = forms.IntegerField(initial=2017,min_value=2017,max_value=2100)
