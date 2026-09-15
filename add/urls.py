from django.urls import path
from . import views

app_name = 'add'

urlpatterns = [
    #添加用户积分
    path('add_score/',views.AddScore,name='add_score'),
]