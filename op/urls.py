from django.urls import path
from . import views

app_name = 'op'
urlpatterns = [
    #管理主页
    path('',views.OpIndex,name='index'),
    #用户管理
    path('user_admin', views.UserAdminIndex, name='user_admin'),
    #修改用户信息
    path('repair_user/(?P<user_name>\d+)/',views.RepairUserInfo,name='repair_user'),
]