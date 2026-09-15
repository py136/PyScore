from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth import logout,login,authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User


def logout_views(request):
    '''用户注销'''
    logout(request)
    return HttpResponseRedirect(reverse('check:index'))

def register(request):
    '''用户注册'''
    if request.method != 'POST':
        #显示空的注册表单
        form = UserCreationForm()
    else:
        #处理填写好的表单
        form = UserCreationForm(data = request.POST)

        if form.is_valid():
            new_user = form.save()
            #让用户自动登录，再重定向到主页
            authenticated_user = authenticate(username = new_user.username,password = request.POST['password1'])
            login(request,authenticated_user)
            return HttpResponseRedirect(reverse('check:index'))

    context = {'form':form}
    return render(request,'users/register.html',context)

@login_required
def PersonalIndex(request):
    '''个人中心'''
    user = User.objects.get(username=request.user.username)
    context = {'user':user}

    return render(request,'users/personal_index.html',context)

@login_required
def RepairInfo(request):
    '''修改用户信息'''
    if request.method != 'POST':
        #向用户传递表单及数据
        return render(request,'users/repair_info.html')
    else:
        #处理表单数据
        user = User.objects.get(username = request.user.username)
        user.first_name = request.POST.get('first_name')
        user.last_name = request.POST.get('last_name')
        user.email = request.POST.get('email')
        user.save()
        return HttpResponseRedirect(reverse('users:personal_index'))

