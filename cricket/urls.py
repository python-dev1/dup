

from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [

    path('', views.index,name="home"),
    path('getdata', views.getdata,name="get data"),
    path('uploaddata', views.uploaddata,name="upload data"),
    path('getfile', views.getfile,name="get file"),
    path('uploadfile', views.uploadfile,name="upload file"),
    path('registration', views.registration,name="registration"),
    path('adduser', views.adduser,name="add_user"),
    path('loginuser', views.loginuser,name="loginuser"),
    path('sha256', views.sha256,name="sha256"),
    path('sha1', views.sha1,name="sha1"),
    path('md5', views.md5,name="md5"),
    path('viewfiles', views.viewfiles,name="view_files"),

]



