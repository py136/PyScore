from django.urls import path
from . import views

app_name = 'ranking'

urlpatterns = [
    #进行排名
    path('rank/',views.rank,name='rank'),
]