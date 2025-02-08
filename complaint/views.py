from django.shortcuts import render
from .models import Complaint_Score_Details,Complaint_Score_Details_History,Complaint_Score_Details_History_User
from check.models import Score_all
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.urls import reverse
from datetime import datetime

@login_required
def Complaint(request,entry_id):
    '''用户提交申诉请求'''
    entry = Score_all.objects.get(id = entry_id)
    signal = 'now:' + datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')
    if entry.owner != request.user:return render(request,'complaint/403.html')#确认该条目属于当前用户     
    else:
        if request.method == 'GET':
            #处理用户提交请求
            context = {'entry':entry}
            return render(request,'complaint/complaint_detail.html',context)
        elif request.method == 'POST':
            #对用户请求进行处理
            detail = Complaint_Score_Details(text = entry.text,score = entry.score,
                                           owner = entry.owner,reason = request.POST.get('reason'),
                                           original_id = entry_id,state = '待处理',sign = signal)#对输入进行处理
            detail_user = Complaint_Score_Details_History_User(text = entry.text,score = entry.score,
                                           owner = entry.owner,reason = request.POST.get('reason'),
                                           state = '待处理',sign = signal)
            detail.save()
            detail_user.save()
            return HttpResponseRedirect(reverse('check:entry',args = [entry.topic.id]))
        

@login_required
def check_complaint_details(request):
    '''将申诉条目呈现给审核者'''
    user_groups = set(request.user.groups.all().values_list('name', flat=True))
    
    # 定义需要检查的组名
    required_groups = {'monitor_users', 'super_users'}
    
    # 检查当前用户是否属于任何一个必需的组
    if required_groups.intersection(user_groups):
        #从数据库中获取数据
        entries = Complaint_Score_Details.objects.all()
        context = {'entries':entries}
        return render(request,'complaint/check_complaint_details.html',context)
    
    else:
        return render(request,'complaint/403.html')
    
@login_required
def complaint_index(request):
    '''申诉主页'''
    user_groups = set(request.user.groups.all().values_list('name', flat=True))
    
    # 定义需要检查的组名
    required_groups = {'monitor_users', 'super_users'}
    
    # 检查当前用户是否属于任何一个必需的组
    if required_groups.intersection(user_groups):return render(request,'complaint/complaint_index.html')
    else:return render(request,'complaint/403.html')

@login_required
def deal_complaint_detail(request,entry_id):
    '''处理申诉的条目'''
    user_groups = set(request.user.groups.all().values_list('name', flat=True))
    
    # 定义需要检查的组名
    required_groups = {'monitor_users', 'super_users'}
    
    # 检查当前用户是否属于任何一个必需的组
    if required_groups.intersection(user_groups):
        entry = Complaint_Score_Details.objects.get(id=entry_id)
        context = {'entry':entry}
        if request.method == 'GET':
            #发送表单
            return render(request,'complaint/deal_complaint_detail.html',context)
        
        elif request.method == 'POST':
            #对表单进行处理
            if request.POST.get('deal') == 'yes':
                #同意撤销，对数据进行处理
                complaint_entry_history=Complaint_Score_Details_History(score = entry.score,
                                                                        text = entry.text,owner = entry.owner,
                                                                        reason = entry.reason,state = '不通过')#对审核者的历史记录进行处理
                complaint_entry_user = Complaint_Score_Details_History_User.objects.get(sign = entry.sign)
                complaint_entry_user.state = '通过'#对用户的历史记录进行更新
                orginal_entry = Score_all.objects.get(id = entry.original_id)
                complaint_entry_history.save()
                complaint_entry_user.save()
                entry.delete()
                orginal_entry.delete()#对申诉条目进行删除
                return HttpResponseRedirect(reverse('complaint:check_complaint_details'))

            elif request.POST.get('deal') == 'no':
                #不同意撤销，对数据进行处理
                complaint_entry_history = Complaint_Score_Details_History(score = entry.score,
                                                                        text = entry.text,owner = entry.owner,
                                                                        reason = entry.reason,state = '不通过')#对审核者的历史记录进行处理
                complaint_entry_user = Complaint_Score_Details_History_User.objects.get(sign = entry.sign)
                complaint_entry_user.state = '不通过'#对用户的历史记录进行更新
                complaint_entry_history.save()
                complaint_entry_user.save()
                entry.delete()
                return HttpResponseRedirect(reverse('complaint:check_complaint_details'))

    else:return render(request,'complaint/403.html')

@login_required
def check_complaint_histories(request):
    ''''审核者查看已完成的项目'''
    user_groups = set(request.user.groups.all().values_list('name', flat=True))
    
    # 定义需要检查的组名
    required_groups = {'monitor_users', 'super_users'}
    
    # 检查当前用户是否属于任何一个必需的组
    if required_groups.intersection(user_groups):
        #从数据库中获取数据
        entries = Complaint_Score_Details_History.objects.all()
        context = {'entries':entries}
        return render(request,'complaint/check_complaint_histories.html',context)
    else:return render(request,'complaint/403.html')


@login_required
def check_complaint_histories_user(request):
    '''用户查看申诉记录'''
    entries = Complaint_Score_Details_History_User.objects.filter(owner = request.user).order_by('date_added')
    context = {'entries':entries}
    return render(request,'complaint/check_complaint_his.html',context)
