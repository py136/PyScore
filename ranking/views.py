from django.shortcuts import render
from .models import Ranking_Scores
from django.contrib.auth.decorators import login_required
from check.models import Score_all,Score_Topics,Scores_Histories
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.urls import reverse

@login_required
def rank(request):
    '''计算用户排名'''
    # 获取当前用户所属的所有组
    user_groups = set(request.user.groups.all().values_list('name', flat = True))
    
    # 定义需要检查的组名
    required_groups = {'monitor_users', 'super_users'}
    
    # 检查当前用户是否属于任何一个必需的组
    if required_groups.intersection(user_groups):
        if request.method == 'GET':
            #发送确认表单
            return render(request,'ranking/rank.html')
        
        elif request.method == 'POST':
            users = User.objects.all()
            #读取数据并存入Ranking_Scores中
            for user in users:
                entries = Score_all.objects.filter(owner = user).order_by('date_added')
                scores = []
                for entry in entries:
                    history = Scores_Histories(text = entry.text,owner = user,
                                               score = entry.score,date_added = entry.date_added,)#存入积分历史记录
                    history.save()#存入历史数据
                    scores.append(entry.score)
                    entry.delete()#删除对应数据

                topics = Score_Topics.objects.filter(owner = user).order_by('date_added')
                for topic in topics:topic.delete()#删除积分项
                try:
                    rank_score_old = Ranking_Scores.objects.get(owner = user)
                    rank_score = Ranking_Scores(id = rank_score_old.id,
                                                score = sum(scores),owner = user)
                    rank_score.save()#存入数据
                except BaseException:
                    #若是第一次参与排名，则生成对应数据
                    new_ranking = Ranking_Scores(score = sum(scores),owner = user)
                    new_ranking.save()

            return HttpResponseRedirect(reverse('check:check_rankings'))
                    
    else:return render(request,'ranking/403.html')

