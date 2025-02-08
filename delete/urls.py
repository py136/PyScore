from django.urls import path
from . import views

app_name = 'delete'

urlpatterns = [
    #删除积分项目
    path('delete_score_topic/(?P<topic_id>\d+)/',views.delete_score_topic,name='delete_score_topic'),
    #删除积分细则
    path('delete_score_detail/(?P<entry_id>\d+)/',views.delete_score_detail,name='delete_score_detail'),
    #删除积分历史
    path('delete_histories/',views.delete_histories,name='delete_histories'),
    #删除已申诉的历史记录
    path('delete_complaint_histories/',views.delete_complaint_histories,name='delete_complaint_histories'),
    #用户删除已申诉的历史
    path('delete_complaint_histories_user/',views.delete_complaint_histories_user,
         name='delete_complaint_histories_user'),
]