from django.db import models
from django.contrib.contenttypes import generic
from django.db.models import Q
import os

class PyMonitor(models.Model):

	location = models.TextField('Ubicacion', null=True , blank=True)
	ip =  models.TextField('ip', null=True , blank=True)
	#Cambiar ip por nombrededominio que refiera al pasillo
        description = models.TextField("Descripcion del raspberry pi", max_length=200, null=True, blank=True)


	category = models.ForeignKey("Content")


class Content(models.Model):

	CATEGORY_OPTIONS = (
            (1, 'Anuncios-Mensajes'),
            (2, 'Eventos'),
            (3, 'Avisos'),
            )
	CATEGORY_OPTIONS_DICT = dict(CATEGORY_OPTIONS)
	category = models.IntegerField("Categoria",primary_key=True, max_length=2, choices=CATEGORY_OPTIONS, blank=True)

    	def category_str(self):
        	options = []
        	if self.category:
            		for bit, option in self.CATEGORY_OPTIONS:
                		if bit & self.category:
		                    options.append(option)
        	return options

	description = models.TextField("Descripcion del contenido", max_length=200, null=True, blank=True)

	def save(self, *args, **kwargs):
		filename = self.category_str()
		print self.category_str()
		print filename[self.category-1]
		directory = './intecDisplay_Contenido/' + str(filename[self.category-1])
		
		if not os.path.exists(directory): os.makedirs(directory)
 		super(Content, self).save(*args, **kwargs)

# Create your models here.
