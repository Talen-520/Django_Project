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