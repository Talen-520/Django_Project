from django import forms
from django.forms.widgets import NumberInput

class DemoForm(forms.Form):
    name = forms.CharField(widget=forms.Textarea(attrs={'rows': 2, 'cols': 20}))

class EmailForm(forms.Form):
    Email = forms.EmailField(label="Enter email address", widget=forms.Textarea(attrs={'rows': 2, 'cols': 20}))

class DateForm(forms.Form):
    reservation_date = forms.DateField(widget=NumberInput(attrs={'type': 'date'}))

class ChoiceForm(forms.Form):
    choice = forms.ChoiceField(choices=[('1', 'one'), ('2', 'two'), ('3', 'three')]) # choice = Favorite_dish, example for exisiting database
    #choice = forms.ChoiceField(widget=forms.RadioSelect, choices=[('1', 'one'), ('2', 'two'), ('3', 'three')]) # option 2


SHIFTS= (
    ("1", "morning"),
    ("2", "afternoon"),
    ("3", "evening"),
)
'''
class InputForm(forms.Form):
    first_name = forms.CharField(label='First Name', max_length=100, required=False)
    last_name = forms.CharField(label='Last Name', max_length=100)
    shifts = forms.ChoiceField(choices=SHIFTS)
    time_log = forms.TimeField(help_text='enter exact time ', widget=forms.TimeInput(attrs={'type': 'time'}))
'''

#model form
from .models import Logger
class LogForm(forms.ModelForm):
    class Meta:
        model = Logger
        fields = '__all__' #import all fields from model
            #or customized fields with ['first_name', 'last_name', 'time_log']


#reservations form has no html presented, in the admin page, it is presented in a table
from .models import survey   
from django.core.validators import RegexValidator
class surveyForm(forms.ModelForm):
    phone = forms.CharField(
        label="Phone number:",
        max_length=10,
        validators=[
            RegexValidator(
                regex=r'^[0-9]{10}$',
                message="Enter a valid US phone number starting with +1.",
            ),
        ],
            widget=forms.TextInput(attrs={'placeholder': '0123456789'}),
        )
    comments = forms.CharField(
        widget=forms.Textarea(attrs={'rows': 5, 'placeholder': 'Enter your comments here'}),
        max_length=100,
        required=True,
    )
    class Meta:
        model = survey
        fields = '__all__'
        #widgets = {
        #    'comments': forms.Textarea(attrs={'rows': 5, 'cols': 45}),
        #}

from .models import userinformation
class userform(forms.ModelForm):
    class Meta:
        model = userinformation
        fields = '__all__'
