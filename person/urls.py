from django.urls import path
from . import views

app_name = 'person'
urlpatterns = [
    #用户中心主页
    path('person/',views.person_index,name = 'person'),
    #修改个人信息
    path('repair_info/',views.repair_info,name='repair_info'),
]