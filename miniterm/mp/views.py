from datetime import datetime
from PIL import Image
import io


from .models import *  
from .forms import UploadFileForm

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.http import JsonResponse
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.core.files.storage import FileSystemStorage
from django.contrib.auth import get_user_model
from django.core.files.base import ContentFile

User = get_user_model()

def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        
        if user is not None:
            login(request, user)
            #return JsonResponse({'status': '200', 'message': '登录成功'})
            return render(request, 'face/show.html')
        else:
            #return JsonResponse({'status': '400', 'message': '用户名或密码错误'})
            return render(request, 'user/login.html', {'error_message': '用户名或密码错误'})
    return render(request, 'user/login.html')


def register_view(request):
    return render(request, 'user/register/register.html')

def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        print
        password = request.POST['password']
        contactinfo = request.POST['email']
    if not (username and password and contactinfo):
        return JsonResponse({'status': '400', 'message': '缺少信息'})
    if User.objects.filter(username = username).exists():
        return JsonResponse({'status': '400', 'message': '用户名已存在'})
    current_time = datetime.now()
    formated_time = current_time.strftime('%Y-%m-%d')
    user = User.objects.create_user(username=username, password=password,
                                    role = 'Admin', accesslevel = 0, contactinfo = contactinfo,
                                    authorizationdate = formated_time)

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
    
    user = User.objects.create_user(username=username, password=password, role = role, 
                                    accesslevel = accesslevel, contactinfo = contactinfo, 
                                    authorizationdate = formated_time)
    data = {
        'id': user.id,
        'username': username,
        'password': password,
        'role': role,
        'accesslevel': accesslevel,
        'contactinfo': contactinfo,
        'authorizationdate': formated_time
    }

    return JsonResponse({'status': '200', 'message': '添加成功', 'data': data})

@login_required
def UserDelete(request):
    if request.method == 'POST':
        id = request.POST['id']
    if not id:
        return JsonResponse({'status': '400', 'message': '缺少信息'})
    user = User.objects.get(id=id)
    user.delete()
    return JsonResponse({'status': '200', 'message': '删除成功'})



#@login_required
def logtemphum_and_face(request):
    
    all_info = TempAndHum.objects.all()

    sensor_data = [
        {
            "temperature": record.temperature,  
            "humidity": record.humidity,        
            "time": record.time,  
        }
        for record in all_info
    ]
    
    all_info = FaceRecognitionLogs.objects.all()
    logs = []
    for record in all_info:
        userid = record.userid.id
        name = AccessPeople.objects.get(id = userid).name
        time = record.time
        result = record.result
        logs.append({
            "name": name,
            "time": time,
            "result": result
        })
    
    
    all_info = FaceRecognitionLogs.objects.all()
    logs = []
    for record in all_info:
        userid = record.userid.id
        name = AccessPeople.objects.get(id = userid).name
        time = record.time
        result = record.result
        logs.append({
            "name": name,
            "time": time,
            "result": result
        })
    #return JsonResponse({'status': '200', 'message': '', 'data': logs})
    return render(request, 'logs/log.html', {'face_logs': logs, 'tem_logs': sensor_data})



#@login_required
def showface(request):
    all_info = AccessPeople.objects.all()

    data =[
        {
            "id": record.id,
            "name": record.name,
            "face_url": record.imageurl,
        }
        for record in all_info
    ]
    #return JsonResponse({'status': '200', 'message': '', 'data': data})
    return render(request, 'face/show.html', {'datas': data})


#增加人脸识别信息
#@login_required
def addface(request):
    if request.method == 'POST':
        
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            name = form.cleaned_data['name']
            face_image = request.FILES['face_image']

            image = Image.open(face_image)
            image = image.convert('RGB')  
            
            
            image_io = io.BytesIO()
            image.save(image_io, format='JPEG')  
            image_io.seek(0)  
            
            fs = FileSystemStorage()
            filename = f"{name}.jpg"  
            file_url = fs.save(filename, ContentFile(image_io.read()))  
            
            accesspeople = AccessPeople.objects.create(name=name, imageurl=fs.url(file_url))
            return JsonResponse({'status': '200',
                                'message': '上传成功',
                                'data': {
                                    'id': accesspeople.id,
                                    'name': name,
                                    'face_url': file_url
                                }
                                })
        else:
            return JsonResponse({'status': '400', 'message': '上传失败，请检查格式'})
        
#@login_required
def deleteface(request):
    if request.method == 'POST':
        id = request.POST['id']
        if not id:
            return JsonResponse({'status': '400', 'message': '缺少信息'})
        face = AccessPeople.objects.get(id=id)
        face.delete()
        return JsonResponse({'status': '200', 'message': '删除成功'})
    

#@login_required
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

#@login_required
def getdevice(request):
    all_info = DeviceStatus.objects.all()
    data = [
        {
            "id": record.deviceID,
            "DeviceName": record.deviceName,
        }
        for record in all_info
    ]
    #return JsonResponse({'status': '200', 'message': '', 'data': data})

    return render(request, 'control/control.html', {'datas': data})



def gethumandtemp(request):
    if request.method == 'POST':
        temperature = request.POST['temperature']
        humidity = request.POST['humidity']
    
    format_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    TempAndHum.objects.create(temperature=temperature, humidity=humidity, time=format_time)

    return JsonResponse({'status': '200', 'message': '上传成功'})


def getcamera(request):
    
    #image = request.FILES['image']
    # if isFace(image):
        
    #     #TODO: 人脸识别
    #     #识别成功后，将识别结果存入数据库
    #     pass
    # else:
    format_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    accesspeople = AccessPeople.objects.get(id = 3)
    FaceRecognitionLogs.objects.create(userid = accesspeople, time = format_time, result='success')

    return JsonResponse({'status': '200', 'message': '上传成功'})