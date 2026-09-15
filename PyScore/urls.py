"""PyScore URL Configuration

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
    path('users/',include('users.urls',namespace='users')),#用户登录/注册服务
    path('op/',include('op.urls',namespace='op')),#管理
    path('add/',include('add.urls',namespace='add')),#"添加"功能
    path('complain/',include('complain.urls',namespace='complain')),#申诉功能
    path('ranking/',include('ranking.urls',namespace='ranking')),#排名功能

]
