from django.shortcuts import render
from .models import ScoreEntries,Scores
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from op.authority import CheckAuthority,Send403
from complain.models import ComplainDetails
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.urls import reverse

# Create your views here.


def index(request):
    '''项目首页'''
    return render(request,'check/index.html')

@login_required
def CheckEntry(request):
    '''用户查看积分详细条目'''
    entries = ScoreEntries.objects.filter(owner=request.user).order_by('date_added')
    try:
        score = Scores.objects.get(owner=request.user)
        context = {'entries':entries, 'score':score.score}

    except Scores.DoesNotExist:
        context = {'entries':entries, 'score':0}



    return render(request,'check/entry.html',context)

@login_required
def CheckUsers(request):
    '''查看所有用户积分'''
    
    #检查用户权限
    if CheckAuthority(request):
        # 获取所有用户
        users = User.objects.all()
        context = {'users':users}

        return render(request,'check/users.html',context)
    
    else:
        return Send403(request)

@login_required
def CheckDetails(request,user_name):
    '''查看用户详细积分情况'''
    
    #检查用户权限
    if CheckAuthority(request):
        # 获取单个用户的积分主题
        user = User.objects.get(username=user_name)
        entries = ScoreEntries.objects.filter(owner=user).order_by('date_added')
        try:
            score = Scores.objects.get(owner=user)
            context = {'entries':entries,'tar_user':user,'score':score.score}

        except Scores.DoesNotExist:
            context = {'entries':entries,'tar_user':user,'score':0}

        return render(request,'check/user_details.html',context)
    
    else:
        return Send403(request)
    
@login_required
def CheckComplain(request):
    '''查看申诉'''

    #检查用户权限
    if CheckAuthority(request):
        #获取全部申诉条目
        complaints = ComplainDetails.objects.all()

        context = {'complaints':complaints}
        return render(request,'check/complaints.html',context)

    else:
        return Send403(request)

@login_required
def UserInfo(request, user_name):
    '''查看用户信息'''

    #检查用户权限
    if CheckAuthority(request):
        try:
            user = User.objects.get(username=user_name)

        except User.DoesNotExist:
            messages.error(request, '此用户不存在')

            return HttpResponseRedirect(reverse('op:user_admin'))

        groups = user.groups.all()    #获取用户组

        context = {'tar_user':user, 'groups':groups}

        return render(request, 'check/user_info.html', context)
    
    else:
        return Send403(request)
    