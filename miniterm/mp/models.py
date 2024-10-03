from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    role = models.CharField(max_length=100)
    accesslevel = models.IntegerField()
    contactinfo = models.CharField(max_length=100)
    authorizationdate = models.DateField()


class AccessLoggs(models.Model):
    logID = models.IntegerField(primary_key=True)
    userID = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    accesstime = models.DateTimeField()
    status = models.IntegerField()

class DeviceStatus(models.Model):
    deviceID = models.IntegerField(primary_key=True)
    deviceName = models.CharField(max_length=100)
    status = models.CharField(max_length=50)
    lastupdate = models.DateTimeField()

class Sensor(models.Model):
    sensorID = models.IntegerField(primary_key=True)
    deviceid = models.ForeignKey(DeviceStatus, on_delete=models.DO_NOTHING,to_field='deviceID')
    sensortype = models.CharField(max_length=50)
    value = models.FloatField()

class EventLogs(models.Model):
    eventid = models.IntegerField(primary_key=True)
    eventtype = models.CharField(max_length=50)
    eventtime = models.DateTimeField()
    description = models.TextField(max_length=200)
    device_id = models.ForeignKey(DeviceStatus, on_delete=models.DO_NOTHING,to_field='deviceID')


class TempAndHum(models.Model):
    temperature = models.IntegerField()
    humidity = models.IntegerField()
    time = models.DateTimeField()


class AccessPeople(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.TextField(max_length=100)
    imageurl = models.CharField(max_length=100)
    
class FaceRecognitionLogs(models.Model):
    recongnitionid = models.AutoField(primary_key=True)
    userid = models.ForeignKey(AccessPeople, on_delete=models.DO_NOTHING)
    time = models.DateTimeField()
    result = models.CharField(max_length=50)