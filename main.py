from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

import os
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile
from django.conf import settings
from forgery_app.models import User
from django.db.models import Q
from forgery_app import process
import shutil
import os


# Creating views

def login(request):
    if request.method == 'POST':
        login_id = request.POST['loginId']
        password = request.POST['password']

        user = User.objects.filter(email=login_id, password=password).first()

        if user is None:
            return render(request, 'index.html', {'error': 'Invalid Login Credentials'})
        else:
            return render(request, 'home.html')
    else:
        return render(request, 'index.html')


def register(request):
    if request.method == 'POST':

        name = request.POST['name']
        contact = request.POST['contact']
        email = request.POST['email']
        password = request.POST['password']

        user = User.objects.filter(
            Q(contact=contact) | Q(email=email)
        ).first()

        if user != None and user.contact == contact:
            return render(request, 'register.html', {'error': 'Duplicate Contact'})

        if user != None and user.email == email:
            return render(request, 'register.html', {'error': 'Duplicate Email'})

        user = User(full_name=name, contact=contact,
                    email=email, password=password)
        user.save()

        return render(request, 'register.html', {'mes': 'Registered Successfully'})
    else:
        return render(request, 'register.html')


def home(request):

    if request.method == "GET":
        return render(request, 'home.html')

    if request.method == "POST":
        image = request.FILES['image']

        shutil.rmtree(os.getcwd() + '\\media')

        path = default_storage.save(
            os.getcwd() + '\\media\\input.tif', ContentFile(image.read()))

        print(path)

        result = predict.process()

    return render(request, "result.html", {'result': result})