from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('user/login',views.user_login),
    path('user/register_view',views.register_view),
    path('user/register',views.register),
    path('user/add', views.UserAdd),
    path('user/delete', views.UserDelete),
    path('log/faceandtemp', views.logtemphum_and_face),
    path('control/face/show', views.showface),
    path('control/face/add', views.addface),
    path('control/face/delete', views.deleteface),
    path('control/device', views.controldevice),
    path('control/device/list', views.getdevice),
    path('hardware/temp', views.gethumandtemp),
    path('hardware/camera', views.getcamera),
]