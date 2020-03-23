from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from .forms import NewUserForm
import pyautogui as AG


# Create your views here.

def homepage(request):
    return render(request=request,
                  template_name="remoteController/home.html",
                  context={})


@login_required(login_url='/login/')
def account(request):
    # if not request.user.is_authenticated:
    #     return redirect(to="remoteController:login")
    # else:
    return render(request=request,
                  template_name="remoteController/account.html",
                  # context={"categories":TutorialCategory.objects.all}
                  ) 


def register(request):
    if request.method == "POST":  # para apanhar o submit depois de carregar no botão
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = form.save()  # aqui criamos o user
            # agora depois de registar temos que o logar automaticamente
            username = form.cleaned_data.get('username')
            messages.success(request=request,
                             message=f"New Account Created {username}")
            login(request, user)
            messages.info(request=request, message=f"You are now logged in as {username}")
            return redirect(
                to="remoteController:homepage")
        else:
            for msg in form.error_messages:
                messages.error(request=request, message=f"{msg}: {form.error_messages[msg]}")

    form = NewUserForm
    return render(request=request,
                  template_name="remoteController/register.html",
                  context={"form": form})


def logout_request(request):
    logout(request=request)
    messages.info(request=request, message="Logged out successfully!")
    return redirect(to="remoteController:homepage")


def login_request(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')  # ('fieldname')
            password = form.cleaned_data.get('password')
            # user = authenticate(request=request,username=username,password=password) ou ??
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request=request, message="Logged in successfully!")
                return redirect("remoteController:homepage")
            else:
                messages.error(request, "Invalid username or password")
        else:
            messages.error(request, "Invalid username or password")

    form = AuthenticationForm()
    return render(request=request,
                  template_name="remoteController/login.html",
                  context={"form": form})


def autoGuiTest(request):
    print("moved")
    # AG.moveTo(100, 200)
    return render(request, 'remoteController/autoGuiTest.html')


def likePost(request):
    if request.method == 'GET':
        try:
            post_id = request.GET['post_id']
        except:
            post_id = None

        try:
            text2write = request.GET['fname']
        except:
            text2write = None

        if text2write is not None:
            AG.write(text2write)
            return HttpResponse("Success!")  # Sending an success response

        try:
            speed = int(request.GET['speed'])
        except:
            speed = None

        if post_id == 'MouseUP':
            AG.moveRel(0, -speed)
        elif post_id == 'MouseRIGHT':
            AG.moveRel(speed, 0)
        elif post_id == 'MouseDOWN':
            AG.moveRel(0, speed)
        elif post_id == 'MouseLEFT':
            AG.moveRel(-speed, 0)
        elif post_id == 'ClickLEFT':
            AG.leftClick()
        elif post_id == 'ClickRIGHT':
            AG.rightClick()
        elif post_id == 'ArrowRIGHT':
            AG.press('right')
        elif post_id == 'ArrowLEFT':
            AG.press('left')
        elif post_id == 'ArrowUP':
            AG.press('up')
        elif post_id == 'ArrowDOWN':
            AG.press('down')
        elif post_id == 'Backspace':
            AG.press('backspace')
        elif post_id == 'Enter':
            AG.press('enter')
        elif post_id == 'ScrollUP':
            AG.scroll(clicks=int(speed * 2))
        elif post_id == 'ScrollDOWN':
            AG.scroll(clicks=int(-speed * 2))

        return HttpResponse("Success!")  # Sending an success response
    else:
        return HttpResponse("Request method is not a GET")
