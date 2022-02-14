from django.shortcuts import render
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from .forms import ContactForm
from django.conf import settings

def contact_view(request):
    newline='\n'
    if request.method == 'POST':
            form = ContactForm(request.POST)
            if form.is_valid():
                form.save()
                email_subject = f'{form.cleaned_data["eposta"]}: {form.cleaned_data["isim"]} bir CM2 sözlüğü önerisi gönderdi.'
                email_message = (f" Değiştirilecek/Eklenecek Terim/Kısaltma : {form.cleaned_data['degisim']} {newline}"
                                 f" Problem tanımı:{form.cleaned_data['problem']} {newline}"
                                 f" Öneri:{form.cleaned_data['oneri']}")
                send_mail(email_subject, email_message, settings.CONTACT_EMAIL, settings.ADMIN_EMAIL)
                return render(request, 'success.html')
    form = ContactForm()
    context = {'form': form}
    return render(request, 'contact.html', context)
