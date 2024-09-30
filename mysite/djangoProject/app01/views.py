from django.shortcuts import render, HttpResponse, redirect

from .models import UserInfo


def index(request):
    return HttpResponse("欢迎使用")

def user_list(request):
    return render(request, "user_list.html")

def user_add(request):
    return render(request, "user_add.html")

def tpl(request):
    name  = "韩超"
    roles = ["管理员", "CEO" ,"保安"]
    user_info = {"name": "郭志", "salary":100000, 'role': "CEO"}

    data_list = [
        {"name": "郭志", "salary": 100000, 'role': "CEO"},
        {"name": "卢辉", "salary": 100000, 'role': "CEO"},
        {"name": "赵建先", "salary": 100000, 'role': "CEO"},

    ]
    return render (request, 'tpl.html', {"n1": name, "n2":roles, "n3":user_info, "n4":data_list})

def something(request):
    print(request.method)
    print(request.GET)
    print(request.POST)
    return redirect("www.baidu.com")

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