from datetime import datetime

from .models import *  
from .forms import UploadFileForm

from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.http import JsonResponse
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.core.files.storage import FileSystemStorage




def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        
        if user is not None:
            login(request, user)
            return JsonResponse({'status': '200', 'message': '登录成功'})
        else:
            return JsonResponse({'status': '400', 'message': '用户名或密码错误'})




def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        contactinfo = request.POST['contactinfo']
    if not (username and password and contactinfo):
        return JsonResponse({'status': '400', 'message': '缺少信息'})
    current_time = datetime.now()
    formated_time = current_time.strftime('%Y-%m-%d')
    user = User.objects.create_user(username=username, password=password)
    user.role = 'Admin'
    user.accesslevel = 0
    user.contactinfo = contactinfo
    user.AuthorizationDate = formated_time
    user.save()

    return JsonResponse({'status': '200', 'message': '注册成功'})


@login_required
def UserAdd(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        role = request.POST['role']
        accesslevel = request.POST['accesslevel']
        contactinfo = request.POST['contactinfo']
    
    current_time = datetime.now()
    formated_time = current_time.strftime('%Y-%m-%d')
    
    user = User.objects.create_user(username=username, password=password)
    user.role = role
    user.accesslevel = accesslevel
    user.contactinfo = contactinfo
    user.AuthorizationDate = formated_time
    user.save()

    return JsonResponse({'status': '200', 'message': '添加成功'})

@login_required
def UserDelete(request):
    if request.method == 'POST':
        id = request.POST['id']
    if not id:
        return JsonResponse({'status': '400', 'message': '缺少信息'})
    user = User.objects.get(id=id)
    user.delete()



@login_required
def logtemphum(request):
    
    all_info = TempAndHum.objects.all()
    sensor_data = [
        {
            "temperature": record.temperature,  
            "humidity": record.humidity,        
            "time": record.time,  
        }
        for record in all_info
    ]
    
    return JsonResponse({'status': '200', 'message': '获取成功', 'data': sensor_data})


@login_required
def logface(request):
    
    all_info = FaceRecognitionLogs.objects.all()
    logs = []
    for record in all_info:
        userid = record.userid
        name = AccessPeople.objects.get(id = userid).name
        time = record.time
        result = record.result
        logs.append({
            "name": name,
            "time": time,
            "result": result
        })
    return JsonResponse({'status': '200', 'message': '', 'data': logs})



@login_required
def showface(request):
    all_info = AccessPeople.objects.all()

    data =[
        {
            "id": record.id,
            "name": record.name,
        }
        for record in all_info
    ]
    return JsonResponse({'status': '200', 'message': '', 'data': data})


#增加人脸识别信息
@login_required
def addface(request):
    if request.method == 'POST':
        name = request.POST['name']
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            face_image = request.FILES['face_image']
            fs = FileSystemStorage()
            filename = fs.save(name, face_image)
            file_url = fs.url(filename)
            AccessPeople.objects.create(name=name, face_image=file_url)
            
            return JsonResponse({'status': '200',
                                'message': '上传成功',
                                'data': {
                                    'name': name,
                                    'face_url': file_url
                                }
                                })
        
@login_required
def deleteface(request):
    if request.method == 'POST':
        id = request.POST['id']
        if not id:
            return JsonResponse({'status': '400', 'message': '缺少信息'})
        face = AccessPeople.objects.get(id=id)
        face.delete()
        return JsonResponse({'status': '200', 'message': '删除成功'})
    

@login_required
def controldevice(request):
    if request.method == 'POST':
        DeviceId = request.POST['DeviceId']
        status = request.POST['status']

        #0表示关闭，1表示开启
        #TODO：要传出去电平信号
        deiviceName = DeviceStatus.get(id = DeviceId).DeviceName

        return JsonResponse({
            'status': '200',
            "message": deiviceName + " 已成功" + ("开启" if status == 1 else "关闭")
        })
