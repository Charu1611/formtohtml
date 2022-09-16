from django.shortcuts import render,HttpResponseRedirect,redirect
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate,login as loginUser,logout
from django.contrib.auth.forms import UserCreationForm
from myapp.forms import UploadTemplateForm
from myapp.models import UploadTemplate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login

# Create your views here.
@login_required(login_url='signin')
def home(request):
    if request.user.is_authenticated:
        user=request.user
        form=UploadTemplateForm()
        # todos=ToDo.objects.filter(user=user).order_by('priority')
        return render(request,'index.html',{'form': form,'name':request.user})

def signup(request):
    if request.method == 'POST':
        fm=UserCreationForm(request.POST or None)
        if fm.is_valid():
            messages.success(request,'Account created Successfully')
            user=fm.save()
            if user is not None:
                return redirect('/signin/')
    else:
        fm=UserCreationForm()
    return render(request,'signup.html',{'form':fm})

def signin(request):
        if request.method == 'POST':
            fm=AuthenticationForm(request=request,data=request.POST)
            if fm.is_valid():
                uname=fm.cleaned_data['username']
                upass=fm.cleaned_data['password']
                user=authenticate(username=uname,password=upass)
                if user is not None:
                    loginUser(request, user)
                    messages.success(request,'Successfully logged in!')
                    return redirect('home')
        else:
            fm=AuthenticationForm()
        return render(request, 'signin.html',{'form':fm})

def signout(request):
    logout(request)
    return redirect('home')


@login_required(login_url='signin')
def add_details(request):
    if request.user.is_authenticated:
        data=UploadTemplate.objects.all()
        user = request.user
        form = UploadTemplateForm(request.POST,request.FILES)
        if form.is_valid():
            todo = form.save(commit=False)
            todo.user = user
            todo.save()
            return redirect("home")
        else: 
            return render(request , 'index.html' , {'form' : form, 'data' :data})
