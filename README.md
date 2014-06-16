intecDisplay
============

INSTALL

Crear carpetas e instalar ambiente

1.- mkdir ~/apps
2.- cd ~/apps/
3.- git clone https://github.com/aqt01/intecDisplay.git
4.- cd intecDisplay

> Instala los packetes necesarios en python para subir el servidor

5.- pip install -r deploy/requirements.txt 

> Crea el usuario admin para entrar al servidor

6.- python manage.py createsuperuser

> Corre el servidor en 127.0.0.1:8080 
 
7.- python manage.py runserver 8080

> Para ver el panel de administrador, entre desde cualquier buscador a 127.0.0.1:8080/admin y entre con la cuenta creada en el paso 6


