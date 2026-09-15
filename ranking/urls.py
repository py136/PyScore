from django.urls import path
from . import views

app_name = 'ranking'

urlpatterns = [
    path('api/my-rank/', views.my_rank_api, name='my_rank_api'),
    path('', views.leaderboard, name='leaderboard'),      # 排行榜首页
]