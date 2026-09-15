from django.urls import path
from . import views

app_name = 'complain'

urlpatterns = [
    #申诉积分
    path('complain_detail/(?P<entry_id>\d+)/',views.ComplainDetail,name='complain_detail'),
    #处理申诉
    path('deal_complaint/(?P<complaint_id>\d+)/',views.DealComplain,name='deal_complaint'),
    #撤销积分
    path('delete_score/(?P<entry_id>\d+)/',views.DeleteScore,name='delete_score'),
]