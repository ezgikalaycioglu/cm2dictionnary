from .models import *
from django.forms import ModelForm
from django import forms

class TermsForm(forms.ModelForm):
    model = Term
    fields = ('tr', 'eng', 'tnm', 'dfn')
