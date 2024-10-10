from django.shortcuts import render, HttpResponse, redirect

from django.contrib.auth import authenticate, login

from .models import UserInfo

from .forms import LoginForm

from .forms import RegistrationForm


def info_list(request):
    data_list = UserInfo.objects.all()
    print(data_list)
    return render(request, "info_list.html" ,{"data_list":data_list})

def info_add(request):
    if request.method == "GET":
        return render(request , "info_add.html")
    user = request.POST.get("user")
    pwd=request.POST.get("pwd")
    age=request.POST.get("age")
    UserInfo.objects.create(user=user, password=pwd,age=age)
    return redirect("http://127.0.0.1:8000/info/list/")

def info_delete(request):
    nid=request.GET.get("nid")
    UserInfo.objects.filter(id=nid).delete()
    return redirect("http://127.0.0.1:8000/info/list/")

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('info_list')
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})

def home(request):
    return render(request, 'home.html')

def register_view(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            # 注册后自动登录
            user = authenticate(username=form.cleaned_data['username'], password=form.cleaned_data['password1'])
            if user is not None:
                login(request, user)
                return redirect('info_list')
    else:
        form = RegistrationForm()
    return render(request, 'register.html', {'form': form})