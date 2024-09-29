from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('/user/login',views.login),
    path('/user/register',views.register),
    path('/user/add', views.UserAdd),
    path('/user/delete', views.UserDelete),
    path('/log/temp', views.logtemphum),
    path('/log/face', views.logface),
    path('/log/face/show', views.showface),
    path('/control/face/add', views.addface),
    path('/control/face/delete', views.deleteface),
    path('/control/device', views.controldevice),
    path('/hardware/temp', views.gethumandtemp),
    path('/hardware/camera', views.getcamera),
]