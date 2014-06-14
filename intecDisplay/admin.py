from django.contrib import admin
from django.contrib.admin import site, ModelAdmin
from intecDisplay.models import PyMonitor, Content, ContentCategory, Location
from django import forms

class PyMonitorAdmin(ModelAdmin):
	list_display = ('location','ip','description',)


class ContentCategoryAdmin(ModelAdmin):
	list_display = ('category', 'description')

class LocationAdmin(ModelAdmin):
	list_display = ('building','corridor')

class ContentAdmin(ModelAdmin):
	list_display = ('photo',)


site.register(PyMonitor, PyMonitorAdmin)
site.register(Content, ContentAdmin)
site.register(ContentCategory, ContentCategoryAdmin)
site.register(Location, LocationAdmin)


# Register your models here.
