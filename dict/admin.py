from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from import_export import resources, widgets, fields
from import_export.admin import ImportExportModelAdmin, ImportExportActionModelAdmin
from .models import *
# Register your models here.

# admin.site.register(item)
@admin.register(Terms)
class ViewAdmin(ImportExportModelAdmin):
    list_display= ('id', 'tr', 'eng')

@admin.register(Abr)
class ViewAdmin(ImportExportModelAdmin):
    list_display= ('id', 'abr', 'meaning')
