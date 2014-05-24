from django.contrib import admin
from django.contrib.admin import site, ModelAdmin
from intecDisplay.models import PyMonitor

class PyMonitorAdmin(ModelAdmin):
	pass

site.register(PyMonitor, PyMonitorAdmin)

# Register your models here.
