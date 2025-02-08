from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.models import User

@login_required
def person_index(request):
    '''用户中心主页'''
    user = User.objects.get(username = request.user.username)
    context = {'user':user}
    return render(request,'person/person_index.html',context)

@login_required
def repair_info(request):
    '''修改用户信息'''
    if request.method == 'GET':
        #向用户传递表单及数据
        return render(request,'person/repair_info.html')
    elif request.method == 'POST':
        #处理表单数据
        user = User.objects.get(username = request.user.username)
        user.first_name = request.POST.get('first_name')
        user.last_name = request.POST.get('last_name')
        user.email = request.POST.get('email')
        user.save()
        return HttpResponseRedirect(reverse('person:person'))

