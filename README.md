# Remote-Controller-Browser2Host
Control the webservice host through a web browser

Installation steps:\
To create a new secret key

```
Google "django secret key generator" to create your own key
The file "secret_secrets.txt" should have just one line containing the "SECRET_KEY"
Path for "secret_secrets.txt" should be "ProjectRootFolder/ProjectMysite/secret_secrets.txt"
In other words, it should be right next to "manage.py" (aka in same location/folder of the file "manage.py")
```

run: python manage.py runserver 0.0.0.0:8000

To access the website go to a browser and type in the host ip address followed by the port that the server is running on.\
example:\
http://192.168.1.20:8000/

Powered By:

pack | version
:---: | :---:
Python | 3.6.4
Django | 3.0.4
PyAutoGUI | 0.9.48

The layout can be customized by altering the folders:
```
ProjectMysite/remoteController/views.py
ProjectMysite/remoteController/templates/remoteController/autoGuiTest.html
```
