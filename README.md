intecDisplay
============

Instalacion 


http://hosseinkaz.blogspot.com/2012/06/how-to-install-virtualenv.html




> Instalar ambiente

0.- sudo apt-get update
1.- apt-get install python-setuptools python-dev build-essential git-core -y
2.- easy_install pip
3.- pip install virtualenv
4.- pip install virtualenvwrapper
5.- mkdir ~/.virtualenvs
6.- echo "export WORKON_HOME=~/virtualenvs" >> ~/.bashrc
7.- echo "source /usr/local/bin/virtualenvwrapper.sh" >> ~/.bashrc 
8.- echo "export PIP_VIRTUALENV_BASE=~/virtualenvs" >> ~/.bashrc 
9.- source ~/.bashrc 
10.- mkvirtualenv intecDisplay

El ultimo comando crea y activa el ambiente virtual intecDisplay

> Crear carpetas e instalar intecDisplay

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


