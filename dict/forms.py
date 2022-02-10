from .models import *
from django.forms import ModelForm
from django import forms

class TermsForm(forms.ModelForm):
    model = Terms
    fields = ('tr', 'eng', 'tnm', 'dfn')
