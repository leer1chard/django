from django.urls import path
from . import views

app_name = 'app01'

urlpatterns = [
    path("info/list/", views.info_list),

    path("info/add/", views.info_add),

    path("login/", views.login_view,name="login"),

    path("home/", views.home,name="home"),

    path('register/', views.register_view, name="register"),
]