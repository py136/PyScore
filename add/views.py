from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from check.models import Score_all,Score_Topics
from django.contrib.auth.models import User

@login_required
def new_score(request,topic_id):
    '''添加积分详情'''
    user_groups = set(request.user.groups.all().values_list('name', flat=True))
    
    # 定义需要检查的组名
    required_groups = {'document_users', 'monitor_users', 'super_users'}
    
    # 检查当前用户是否属于任何一个必需的组
    if required_groups.intersection(user_groups):
        top = Score_Topics.objects.get(id = topic_id)
        if request.method == 'GET':
            #若请求为“get”，发送表单
            context = {'topic':top}
            return render(request,'add/new_score.html',context)
        
        elif request.method == 'POST':
            #请求为“POST”，对数据进行处理
            entry = Score_all(score = request.POST.get('score'),
                            text = request.POST.get('detail'),
                            topic = top,owner = top.owner)
            
            entry.save()
            return HttpResponseRedirect(reverse('check:all_details',args=[topic_id]))

    else:
        return render(request,'add/403.html')
    
@login_required
def new_score_topic(request):
    '''为用户添加积分项'''
    user_groups = set(request.user.groups.all().values_list('name', flat=True))
    
    # 定义需要检查的组名
    required_groups = {'document_users', 'monitor_users', 'super_users'}
    
    # 检查当前用户是否属于任何一个必需的组
    if required_groups.intersection(user_groups):
        if request.method == 'GET':
            #发送添加表单
            context={'users':User.objects.all()}
            return render(request,'add/new_score_topic.html',context)
        elif request.method == 'POST':
            #对数据进行存储
            try:
                target_user = User.objects.get(username=request.POST.get('owner'))
            except BaseException:
                context={'user':request.POST.get('owner')}
                return render(request,'add/no_user.html',context)
            else:
                topic=Score_Topics(text = request.POST.get('topic'),owner=target_user)
                topic.save()
                return HttpResponseRedirect(reverse('check:all_score_topics'))
        else:
            return render(request,'add/403.html')
        