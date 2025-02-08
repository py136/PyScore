from django.shortcuts import render,get_object_or_404
from .models import Score_Topics,Score_all,Scores_Histories
from django.contrib.auth.decorators import login_required
from ranking.models import Ranking_Scores

# Create your views here.

def index(request):
    '''score的主页'''
    return render(request,'check/index.html')

@login_required
def check_score_topics(request):
    '''显示计分项'''
    topics = Score_Topics.objects.filter(owner = request.user).order_by('date_added')
    entries = Score_all.objects.filter(owner = request.user).order_by('date_added')#用于计算用户总分
    scores = []
    for entry in entries:scores.append(entry.score)

    context = {'topics':topics,'total':sum(scores)}
    return render(request,'check/score_topics.html',context)

@login_required
def score_detail(request,topic_id):
    '''显示积分详情'''
    topic = get_object_or_404(Score_Topics,id = topic_id)
    if topic.owner != request.user:
        #确认该详情属于当前用户
        return render(request,'check/403.html')
    
    else:
        entries = topic.score_all_set.order_by('-date_added')
        score = []
        for entry in entries:score.append(entry.score)   #计算总分
        context = {'topic':topic,'entries':entries,'total':sum(score)}
        return render(request,'check/entry.html',context)
    
@login_required
def check_all_scores(request):
    '''查看所有用户积分情况'''
    # 获取当前用户所属的所有组
    user_groups = set(request.user.groups.all().values_list('name', flat=True))
    
    # 定义需要检查的组名
    required_groups = {'document_users', 'monitor_users', 'super_users'}
    
    # 检查当前用户是否属于任何一个必需的组
    if required_groups.intersection(user_groups):
        # 获取所有用户的积分主题
        topics = Score_Topics.objects.all()
        context = {'topics': topics}
        return render(request, 'check/all_score_topics.html', context)
    else:
        return render(request, 'check/403.html')
    
@login_required
def check_all_details(request,topic_id):
    ''''查看对应的详情'''
    user_groups = set(request.user.groups.all().values_list('name', flat=True))
    
    # 定义需要检查的组名
    required_groups = {'document_users', 'monitor_users', 'super_users'}
    
    # 检查当前用户是否属于任何一个必需的组
    if required_groups.intersection(user_groups):
       topic = get_object_or_404(Score_Topics,id=topic_id)
       score = []
       entries = topic.score_all_set.order_by('-date_added')
       for entry in entries:score.append(entry.score)      #计算总分
       context = {'topic':topic,'entries':entries,'total':sum(score)}
       return render(request,'check/all_details.html',context)
    else:
        return render(request, 'check/403.html')
    
@login_required
def check_rankings(request):
    '''查看用户排名'''
    # 获取所有用户及其分数
    users_with_scores = Ranking_Scores.objects.all().select_related('owner').order_by('-score')
    
    # 转换为包含用户信息和排名的列表
    rankings = []
    for rank,user_score in enumerate(users_with_scores):
        b = user_score.owner.last_name+user_score.owner.first_name
        a = {'user': b, 'score': user_score.score,'rank': rank + 1}
        rankings.append(a)

    context = {'rankings':rankings}
    user_groups = set(request.user.groups.all().values_list('name', flat=True))
    
    # 定义需要检查的组名
    required_groups = {'monitor_users', 'super_users'}
    
    # 检查当前用户是否属于任何一个必需的组
    if required_groups.intersection(user_groups):
        #根据用户不同，发送不同的页面
        return render(request,'check/check_rankings_a.html',context)
    else:
        return render(request,'check/check_rankings_b.html',context)

@login_required
def check_histories(request):
    '''查看特定用户的积分历史'''
    score_histories = Scores_Histories.objects.filter(owner = request.user).order_by('date_added')
    context = {'entries':score_histories}
    return render(request,'check/check_histories.html',context)
