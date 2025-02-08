from django.urls import path
from . import views

app_name = 'op'
urlpatterns = [
    #管理主页
    path('',views.op_index,name='op'),
]