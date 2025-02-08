from django.urls import path
from . import views

app_name = 'add'

urlpatterns = [
    #添加积分详情
    path('new_score/(?P<topic_id>\d+)/',views.new_score,name='new_score'),
    #添加积分项目
    path('new_score_topic/',views.new_score_topic,name='new_score_topic'),
]