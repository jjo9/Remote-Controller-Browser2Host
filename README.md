# Remote-Controller-Browser2Host
Control the host through a web browser

instalation steps:
creat new secret key

to be acessible from external devices
in settings.py and change the "ALLOWED_HOSTS" line to:
ALLOWED_HOSTS = ['*']
python manage.py runserver 0.0.0.0:8000
