from django.urls import path
from . import views

app_name = 'complaint'

urlpatterns = [
    #用户申诉
    path('complaint_detail/(?P<entry_id>\d+)/',views.Complaint,name='complaint_detail'),
    #审核者查看详细条目
    path('check_complaint_details/',views.check_complaint_details,name='check_complaint_details'),
    #主页
    path('complaint_index',views.complaint_index,name='complaint_index'),
    #审核申诉
    path('deal_complaint_detail/(?P<entry_id>\d+)/',views.deal_complaint_detail,name='deal_complaint_detail'),
    #审核者查看申诉历史
    path('check_complaint_histories/',views.check_complaint_histories,name='check_complaint_histories'),
    #用户查看申诉历史
    path('check_complaint_histories_user/',views.check_complaint_histories_user,name='check_complaint_histories_user'),
]