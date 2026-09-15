from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .authority import CheckAuthority,Send403,CheckOwner
from django.contrib.auth.models import User, Group
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.urls import reverse

# Create your views here.

@login_required
def OpIndex(request):
    '''op主页（用于保护某些限制界面）'''

    #检查用户权限
    if CheckAuthority(request):
        return render(request,'op/op_index.html')
    
    else:
        return Send403(request)


@login_required
def UserAdminIndex(request):
    '''用户管理'''

    #检查用户权限
    if CheckAuthority(request):
        users = User.objects.all()
        context = {'users':users}

        return render(request, 'op/user_admin.html', context)

    else:
        return Send403(request)


@login_required
def RepairUserInfo(request, user_name):
    '''修改用户信息'''

    try:
        #获取要修改的用户信息，便于比对
        user = User.objects.get(username=user_name)
            
    except User.DoesNotExist:
        messages.error(request, '此用户不存在')
        
        return HttpResponseRedirect(reverse('check:user_info', args=[user_name]))

    #检查权限
    if CheckAuthority(request) and not CheckOwner(request, user):

        if request.method != 'POST':
            #发送表单
            
            groups = Group.objects.all()
            current_group = user.groups.first()

            context = {'tar_user':user, 'groups':groups, 'current_group':current_group}

            return render(request, 'op/repair_user.html', context)

        else:
            #对表单进行处理
            target_user = User.objects.get(username=user_name)
            group_id = request.POST.get('group')

            try:
                target_group = Group.objects.get(id=group_id)

            except Group.DoesNotExist:
                messages.error(request, '此用户组不存在')
                return HttpResponseRedirect(reverse('op:repair_user', args=[user_name]))

            target_user.groups.set([target_group])     #更改用户组

            #对用户信息进行更新
            target_user.first_name = request.POST.get('first_name')
            target_user.last_name = request.POST.get('last_name')
            target_user.email = request.POST.get('email')

            target_user.save()     #保存信息

            return HttpResponseRedirect(reverse('check:user_info', args=[user_name]))

    else:
        return Send403(request)