# Remote-Controller-Browser2Host
Control the webservice host through a web browser

<b>Installation steps:</b>\
To create a new secret key

```
Google "django secret key generator" to create your own key
The file "secret_secrets.txt" should have just one line containing the "SECRET_KEY"
Path for "secret_secrets.txt" should be "ProjectRootFolder/ProjectMysite/secret_secrets.txt"
In other words, it should be right next to "manage.py" (aka in same location/folder of the file "manage.py")
```

run: <b>python manage.py runserver 0.0.0.0:8000</b>

To access the website go to a browser and type in the host ip address followed by the port that the server is running on.\
example:\
<b>http://192.168.1.20:8000/</b>

## Authentication 

To add authentication do the following:

To add a user that can be used to login, simply run the following command

<b>python manage.py createsuperuser</b>

In the file <b>"ProjectMysite/remoteController/views.py" </b> \
Uncomment 2 lines with <b>"@login_required(login_url='/login/')"</b> so that only requests made by a logged user are valid

The lines are located above the following functions

```python
@login_required(login_url='/login/')
def likePost(request):

@login_required(login_url='/login/')
def autoGuiTest(request):
```
(To remove authentication just comment those 2 lines)\
Now just login to use the controller

User management can be done in:\
<b>http://website_ip:8000/admin</b>

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
