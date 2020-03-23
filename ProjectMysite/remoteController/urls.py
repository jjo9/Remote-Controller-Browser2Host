"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import path, re_path
from . import views

app_name = "main"

urlpatterns = [
    path("", views.homepage, name="homepage"),  # caminho vazio vai apontar para view homepage
    re_path("^register/?$", views.register, name="register"),
    re_path("^logout/?$", views.logout_request, name="logout"),
    re_path("^login/?$", views.login_request, name="login"),

    re_path("^autoGuiTest/?$", views.autoGuiTest, name="autoGuiTest"), # python auto gui para ver se consigo controlar o pc host com o tel/browser
    re_path(r'^likepost/?$', views.likePost, name='likepost'),  # likepost view at /likepost

    # re_path("^my_blogs/?$", views.my_blogs, name="my_blogs"), # todos podem ver
    # re_path("^public_profile_logged_in/?$", views.public_profile_logged_in, name="public_profile_logged_in"),  # tem que estár logado para ver
    re_path("^account/?$", views.account, name="account"), # apenas o user pode ver

    # re_path("^all_blogPosts_index/?$", views.all_blogPosts_index, name = "all_blogPosts_index"),

    # path('add/', views.add_user_blog_post, name = "add_blog_post"),
    # path('update/<int:blog_post_id>', views.update_user_blog_post, name="update_blog_post"),
    # path('delete/<int:blog_post_id>', views.delete_user_blog_post, name="delete_blog_post"),
    #
    #
    # path("<single_slug>", views.single_slug, name="single_slug"), # <single_slug> está entre <> a indicar que é uma variavel e vamos passa-la para a função
]
