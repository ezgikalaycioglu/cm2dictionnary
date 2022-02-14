from django.contrib import admin

# Register your models here.
from .models import Contact


@admin.register(Contact)
class ViewAdmin(admin.ModelAdmin):
    list_display=('degisim', 'oneri')
