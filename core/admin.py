from django.contrib import admin
from .models import movie
from import_export.admin import ImportExportModelAdmin 
# Register your models here.
#admin.site.register(movie)
@admin.register(movie)
class ViewAdmin(ImportExportModelAdmin):
     pass