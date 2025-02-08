"""Score URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),#大后台
    path('',include('check.urls',namespace='check')),#查看界面
    path('add/',include('add.urls',namespace='add')),#添加
    path('detele/',include('delete.urls',namespace='detele')),#删除
    path('users/',include('users.urls',namespace='users')),#用户登录/注册服务
    path('complaint/',include('complaint.urls',namespace='complaint')),#申诉
    path('person/',include('person.urls',namespace='person')),#用户中心
    path('ranking/',include('ranking.urls',namespace='ranking')),#用户排名
    path('op/',include('op.urls',namespace='op')),#管理页面
]
