from django.shortcuts import render
from . import translate
from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from .forms import *
import pandas as pd
from django.http import HttpResponseRedirect

# Create your views here.

def translator_view(request):
    message=""
    items = Terms.objects.all()
    global data
    data=pd.DataFrame(
        {'id': Terms.objects.values_list('id',flat=True),
         'tr': Terms.objects.values_list('tr',flat=True),
         'eng': Terms.objects.values_list('eng',flat=True),
         'tnm':Terms.objects.values_list('tnm',flat=True),
         'dfn': Terms.objects.values_list('dfn',flat=True)
        })
    if 'submit' in request.POST: #if we press the button
        original_text=request.POST['my_textarea']
        print(original_text)
        output=translate.translate(original_text, data)[0]
        message=translate.translate(original_text, data)[1]
        global dyms
        global lendym
        dyms=translate.translate(original_text, data)[2]
        lendym=(len(dyms))
        print(lendym)
        tnm=translate.translate(original_text, data)[3]
        dfn=translate.translate(original_text, data)[4]
        if output:
            return render(request, 'translator.html', {'output_text':output, 'original_text':original_text, 'message_text':message[0], 'tnm_text':tnm, 'dfn_text':dfn, 'items': items})
        elif lendym:
            return render(request, 'translator.html', {'original_text':original_text, 'dyms':dyms, 'message_text1':message[0], 'message_text2':message[1], 'items': items})
        elif message: #if we refresh the page
            return render(request, 'translator.html',{'message_text':message[0], 'items': items, 'original_text':original_text})
        else:
            #return render(request, 'translator.html')
            return render(request, 'translator.html', {'items': items})
    elif 'didyoumean' in request.POST:
        value= request.POST.get('didyoumean')
        original_text=value
        output=translate.translate(original_text, data)[0]
        message=translate.translate(original_text, data)[1]
        tnm=translate.translate(original_text, data )[3]
        dfn=translate.translate(original_text, data)[4]
        return render(request, 'translator.html', {'output_text':output, 'original_text':original_text, 'message_text':message[0], 'tnm_text':tnm, 'dfn_text':dfn, 'items': items})
    elif 'allterms_translate' in request.POST:
        value= request.POST.get('allterms_translate')
        original_text=value
        output=translate.translate(original_text, data)[0]
        message=translate.translate(original_text, data)[1]
        tnm=translate.translate(original_text, data )[3]
        dfn=translate.translate(original_text, data)[4]
        return render(request, 'translator.html', {'output_text':output, 'original_text':original_text, 'message_text':message[0], 'tnm_text':tnm, 'dfn_text':dfn, 'items': items})
    else: #if we refresh the page
        return render(request, 'translator.html',{'items': items})

def all_terms(request):
    return render(request, 'all_terms.html')

def display_allterms(request):
    items = Terms.objects.all()
    context = {
        'items': items,
    }
    return render(request, 'all_terms.html', context)

def search_allterms(request):
    if request.method == "POST":
        searched= request.POST['searched']
        words=Terms.objects.filter(tr__contains=searched) | Terms.objects.filter(eng__contains=searched)
        return render(request, 'search.html', {'searched':searched, 'words':words})
    else:
        return render(request, 'search.html', {})

def contact_view(request):
    return render(request, 'contact.html')


def all_abbrs(request):
    return render(request, 'abbr.html')

def display_allabbrs(request):
    abrs = Abr.objects.all()
    context = {
        'items': abrs,
    }
    return render(request, 'abbr.html', context)

def search_allabbrs(request):
    if request.method == "POST":
        searched= request.POST['searched']
        words=Abr.objects.filter(abr__contains=searched)
        return render(request, 'searchabbr.html', {'searched':searched, 'words':words})
    else:
        return render(request, 'searchabbr.html', {})
