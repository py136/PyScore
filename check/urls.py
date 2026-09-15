from django.urls import path
from . import views

app_name = 'check'

urlpatterns = [
    #主页
    path('',views.index,name='index'),
    #查看积分
    path('entry/',views.CheckEntry,name='entry'),
    #查看所有用户
    path('users/',views.CheckUsers,name='users'),
    #查看用户积分情况
    path('details/(?P<user_name>\d+)/',views.CheckDetails,name='details'),
    #查看申诉
    path('comlpaints/',views.CheckComplain,name='complaints'),
    #查看用户信息
    path('user_info/(?P<user_name>\d+)/',views.UserInfo,name='user_info'),

]
