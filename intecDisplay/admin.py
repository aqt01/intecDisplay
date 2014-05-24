from django.contrib import admin
from django.contrib.admin import site, ModelAdmin
from intecDisplay.models import PyMonitor, Content
from django import forms

class PyMonitorAdmin(ModelAdmin):
	list_display = ('location','ip','description','category')

class ContentAdmin(ModelAdmin):
	list_display = ('category', 'description')


site.register(PyMonitor, PyMonitorAdmin)
site.register(Content, ContentAdmin)

# Register your models here.
