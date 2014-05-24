from django.db import models

class PyMonitor(models.model):

	location = models.Charfield('Ubicacion', null=True , blank=True)
	ip =  models.Charfield('ip', null=True , blank=True)
	#Cambiar ip por nombrededominio que refiera al pasillo
	category = models.IntegerField("Categoria", max_length=2, null=True, blank=True)
        description = models.CharField("Descripcion del raspberry pi", max_length=200, null=True, blank=True)


CATEGORY_OPTIONS = (
            (1, 'Anuncios/Mensajes'),
            (2, 'Eventos'),
            (3, 'Avisos'),
            )
    CATEGORY_OPTIONS_DICT = dict(CATEGORY_OPTIONS)
    def category_str(self):
        options = []
        if self.category:
            for bit, option in self.CATEGORY_OPTIONS:
                if bit & self.category:
                    options.append(option)
        return options

# Create your models here.
