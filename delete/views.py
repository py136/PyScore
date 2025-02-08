from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from check.models import Score_all,Score_Topics,Scores_Histories
from django.http import HttpResponseRedirect
from django.urls import reverse
from complaint.models import Complaint_Score_Details_History,Complaint_Score_Details_History_User

@login_required
def delete_score_topic(request,topic_id):
    '''删除积分项目'''   
    # 获取当前用户所属的所有组
    user_groups = set(request.user.groups.all().values_list('name', flat = True))
    
    # 定义需要检查的组名
    required_groups = {'document_users', 'monitor_users', 'super_users'}
    
    # 检查当前用户是否属于任何一个必需的组
    if required_groups.intersection(user_groups):
        topic=Score_Topics.objects.get(id = topic_id)
        if request.method == 'GET':
            #发送删除表单
            context = {'topic':topic}
            return render(request,'delete/delete_score_topic.html',context)
        elif request.method == 'POST':
            #对数据进行处理
            entries = topic.score_all_set.order_by('date_added')
            for entry in entries:entry.delete()#删除积分详情
            topic.delete()
            return HttpResponseRedirect(reverse('check:all_score_topics'))

    else:return render(request,'delete/403.html')

@login_required
def delete_score_detail(request,entry_id):
    '''删除积分细则'''
    # 获取当前用户所属的所有组
    user_groups = set(request.user.groups.all().values_list('name', flat = True))
    
    # 定义需要检查的组名
    required_groups = {'document_users', 'monitor_users', 'super_users'}
    
    # 检查当前用户是否属于任何一个必需的组
    if required_groups.intersection(user_groups):
        entry = Score_all.objects.get(id = entry_id)
        topic = entry.topic
        if request.method == 'GET':
            #发送表单
            context={'entry':entry,'topic':topic}
            return render(request,'delete/delete_score_detail.html',context)
        elif request.method == 'POST':
            #对请求进行处理
            print(topic.id)
            entry.delete()
            return HttpResponseRedirect(reverse('check:all_details',args = [topic.id]))   
    else:return render(request,'delete/403.html')


@login_required
def delete_histories(request):
    '''删除积分历史'''
    if request.method == 'GET':
        #向用户发送提交表单
        return render(request,'delete/delete_histories.html')
    
    elif request.method == 'POST':
        #对请求进行处理
        histories = Scores_Histories.objects.filter(owner = request.user).order_by('date_added')
        for history in histories:
            history.delete()#删除对应数据

        return HttpResponseRedirect(reverse('check:check_histories'))
    

@login_required
def delete_complaint_histories(request):
    '''删除已审核的申诉'''
    user_groups = set(request.user.groups.all().values_list('name', flat=True))
    
    # 定义需要检查的组名
    required_groups = {'monitor_users', 'super_users'}
    
    # 检查当前用户是否属于任何一个必需的组
    if required_groups.intersection(user_groups):
        if request.method == 'GET':return render(request,'delete/delete_complaint_histories.html')         #发送表单
        
        elif request.method == 'POST':
            #对请求进行处理
            entires = Complaint_Score_Details_History.objects.all()
            for entry in entires:
                #删除对应数据
                entry.delete()

            return HttpResponseRedirect(reverse('complaint:check_complaint_histories'))

            
    else:return render(request,'delete/403.html')

@login_required
def delete_complaint_histories_user(request):
    '''用户删除自己的申诉历史'''
    if request.method == 'GET':return render(request,'delete/delete_complaint_histories_user.html') #发送表单

    elif request.method == 'POST':
        entries = Complaint_Score_Details_History_User.objects.filter(owner = request.user)
        for entry in entries:
            #删除对应数据
            entry.delete()

        return HttpResponseRedirect(reverse('complaint:check_complaint_histories_user'))