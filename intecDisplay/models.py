from django.db import models
from django.contrib.contenttypes import generic
from django.db.models import Q
import os


class Location(models.Model):
	building = models.CharField('Edificio',max_length=100, null=True , blank=True)
	corridor = models.CharField('Aulas',max_length=150, null=True , blank=True)

	def __unicode__(self):
		return self.building


class ContentCategory(models.Model):
#	CATEGORY_OPTIONS = (
#        	(1, 'Anuncios/Mensajes'),
#       	(2, 'Eventos'),
#           	(3, 'Avisos'),
#            	(4, 'Eventos co-curriculares'),
#            	)

#	CATEGORY_OPTIONS_DICT = dict(CATEGORY_OPTIONS)
#	category = models.IntegerField("Categoria",primary_key=True, max_length=2, choices=CATEGORY_OPTIONS, blank=True)
	category = models.CharField("Categoria",primary_key=True, max_length=100 )

#    	def category_str(self):
#        	options = []
#        	if self.category:
#            		for bit, option in self.CATEGORY_OPTIONS:
#                		if bit & self.category:
#		                    options.append(option)
#        	return options

	description = models.TextField("Descripcion del contenido", max_length=200, null=True, blank=True)
	
	def save(self, *args, **kwargs):
		directory = './intecDisplay_contenido/' + self.category
		print directory
		if not os.path.exists(directory): os.makedirs(directory)
 		super(ContentCategory, self).save(*args, **kwargs)

 	def delete(self, *args, **kwargs):
		directory = './intecDisplay_contenido/' + self.category
		print directory
		os.removedirs(directory)
 		super(ContentCategory, self).delete(*args, **kwargs)

 	def __unicode__(self):
		return self.category

class Content(models.Model):
	contentCategory = models.ManyToManyField(ContentCategory)
	photo = models.ImageField(upload_to='Content')

class PyMonitor(models.Model):

	location = models.ForeignKey(Location)
	ip =  models.CharField('ip', max_length=16,null=True , blank=True)
	#Cambiar ip por nombrededominio que refiera al pasillo
	description = models.TextField("Descripcion del raspberry pi", max_length=200, null=True, blank=True)
	category = models.ManyToManyField("ContentCategory")

	def __unicode__(self):
		return self.ip


# Create your models here.
