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
	category = models.CharField("Categoria",primary_key=True, max_length=100 )
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
	ip =  models.CharField('Ip', max_length=16,null=True,  blank=True)
	username = models.CharField('User', max_length=30,null=True,  blank=True)
	password = models.CharField('Password', max_length=30,null=True,  blank=True)
	description = models.TextField("Descripcion del raspberry pi", max_length=200, null=True, blank=True)
	category = models.ManyToManyField("ContentCategory")

	def save(self, *args, **kwargs):
		# Write user, password and ip in credentials file
		file_path = './intecDisplay_contenido/credentials.txt'
		f = open(file_path, 'wb')
		for p in PyMonitor.objects.all():
			f.write(p.username + ' ' + p.password +  ' ' + p.ip + '\n')
		super(PyMonitor, self).save(*args, **kwargs)

	def delete(self, *args, **kwargs):
		# Used refresh every change 
		file_path = './intecDisplay_contenido/credentials.txt'
		f = open(file_path, 'wb')
		for p in PyMonitor.objects.all():
			f.write(p.username + ' ' + p.password +  ' ' + p.ip + '\n')
 		super(PyMonitor, self).delete(*args, **kwargs)
	
	def __unicode__(self):
		return self.ip