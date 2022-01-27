from django.shortcuts import render
from . import translate

# Create your views here.

def translator_view(request):
    if 'submit' in request.POST: #if we press the button
        original_text=request.POST['my_textarea']
        print(original_text)
        output=translate.translate(original_text)[0]
        message=translate.translate(original_text)[1]
        global dym
        dym=translate.translate(original_text)[2]
        tnm=translate.translate(original_text)[3]
        dfn=translate.translate(original_text)[4]
        #output=original_text.upper()
        return render(request, 'translator.html', {'output_text':output, 'original_text':original_text, 'message_text':message, 'tnm_text':tnm, 'dfn_text':dfn})
    elif 'didyoumean'in request.POST:
        print(dym)
        original_text=dym
        output=translate.translate(original_text)[0]
        message=translate.translate(original_text)[1]
        tnm=translate.translate(original_text)[3]
        dfn=translate.translate(original_text)[4]
        return render(request, 'translator.html', {'output_text':output, 'original_text':original_text, 'message_text':message, 'tnm_text':tnm, 'dfn_text':dfn})
    else: #if we refresh the page
        return render(request, 'translator.html')
