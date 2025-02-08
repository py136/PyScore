from django.urls import path
from . import views

app_name = 'check'

urlpatterns = [
    #主页
    path('',views.index,name='index'),
    #查看积分项
    path('score_topics/',views.check_score_topics,name='score_topics'),
    #查看积分详情
    path('entry/(?P<topic_id>\d+)/',views.score_detail,name='entry'),
    #查看所有用户积分
    path('all_score_topics/',views.check_all_scores,name='all_score_topics'),
    #查看详细内容
    path('all_details/(?P<topic_id>\d+)/',views.check_all_details,name='all_details'),
    #查看用户排名
    path('check_rankings/',views.check_rankings,name='check_rankings'),
    #查看积分历史
    path('check_histories/',views.check_histories,name='check_histories'),
]