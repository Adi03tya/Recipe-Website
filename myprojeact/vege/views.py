from django.shortcuts import render, redirect
from django.contrib import messages 
from django.contrib.auth.models import User
from django.contrib.auth import authenticate , login, logout
from .models import *   
from django.contrib.auth.decorators import login_required

# Create your views here.

def receipe_home(request):
    receipes = Receipe.objects.all()

    if request.GET.get('search'):
        receipes = Receipe.objects.filter(receipe_name__icontains=request.GET.get('search'))
        

    return render(request, "receipe_home.html", {'receipes': receipes})
    

@login_required(login_url='login_page')
def receipe(request):
    
    if request.method != 'POST':
        return render(request, "receipes.html")
    data = request.POST
    receipe_name = data.get('receipe_name')
    receipe_description = data.get('receipe_description')
    receipe_image = request.FILES.get('receipe_image')
    print(receipe_name)
    print(receipe_description)
    Receipe.objects.create(receipe_name=receipe_name, receipe_description=receipe_description, receipe_image=receipe_image,user=request.user)
    if(receipe_name and receipe_description ):
        messages.success(request, 'Receipe added successfully')

    return redirect('receipe')

@login_required(login_url='login_page')
def view_receipe(request):
    receipes = Receipe.objects.filter(user=request.user)

    if request.GET.get('search'):
        receipes = Receipe.objects.filter(receipe_name__icontains=request.GET.get('search'))
        

    return render(request, "view_receipe.html", {'receipes': receipes})

def view_page(request,id):
    receipe = Receipe.objects.get(id=id)
    return render(request, "view_page.html", {'receipe': receipe})

@login_required(login_url='login_page')
def edit_receipe(request,id):
    receipe = Receipe.objects.get(id=id)
    if request.method != 'POST':
        return render(request, "edit_receipe.html", {'receipe': receipe})
    data = request.POST
    receipe_name = data.get('receipe_name')
    receipe_description = data.get('receipe_description')
    receipe_image = request.FILES.get('receipe_image')
    receipe.receipe_name = receipe_name
    receipe.receipe_description = receipe_description
    if receipe_image:
        receipe.receipe_image = receipe_image
    receipe.save()
    return redirect('/view_receipe/')

@login_required(login_url='login_page')
def delete_receipe(request,id):
    receipe = Receipe.objects.get(id=id)
    receipe.delete()
    return redirect('/view_receipe/')


def login_page(request):
    if request.method == 'POST':
        data = request.POST
        username = data.get('username')
        password = data.get('password')
        user = User.objects.filter(username=username).first()
        if user is None:
            messages.error(request, 'Username does not exist')
            return redirect('login_page')
        user = authenticate(request, username=username, password=password)
        if user is None:
            messages.error(request, 'Password is incorrect')
            return redirect('login_page')
        login(request, user)
        return redirect('receipe')
    return render(request, "login.html")

@login_required(login_url='login_page')
def logout_user(request):
    logout(request)
    return redirect('receipe_home')

def register_page(request):

    if request.method == 'POST':
        data = request.POST
        firstname = data.get('firstname')
        lastname = data.get('lastname')
        username = data.get('username')
        email = data.get('email')
        password = data.get('password')
        print(username)
        print(email)
        print(password)
        if User.objects.filter(username=username).exists():
            messages.error(request, 'Username already exists')
            return redirect('register_page')
        user = User.objects.create_user(first_name = firstname, last_name=lastname, username=username, email=email, password=password)
        user.save()
        messages.success(request, 'User registered successfully')
        return redirect('register_page')
    return render(request, "register.html")