from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from op.authority import CheckAuthority,Send403,CheckOwner
from check.models import ScoreEntries,Scores
from django.contrib.auth.models import User
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.urls import reverse

# Create your views here.

@login_required
def AddScore(request):
    '''添加用户积分'''

    #检查用户权限
    if CheckAuthority(request):
        if request.method != 'POST':
            #发送添加表单
            context = {'users':User.objects.all()}

            return render(request,'add/new_score.html',context)
        else:
            #对数据进行处理
            if len(request.POST.get('entry')) > 100:
                #过滤长输入
                messages.error(request,'输入字符超过100字')
                return HttpResponseRedirect(reverse('add:add_score'))
            else:
                #对输入数据进行处理
                try:
                    #判断输入用户是否存在
                    target_user = User.objects.get(username=request.POST.get('owner'))

                except User.DoesNotExist:
                    messages.error(request,'不存在此用户，请重新选择')
                    return HttpResponseRedirect(reverse('add:add_score'))
                
                else:
                    if  not CheckOwner(request, target_user):
                        entry = ScoreEntries(text=request.POST.get('entry'),score=request.POST.get('score'),
                                            owner=target_user)
                        
                        entry.save()
                        
                        try:
                            #对用户总积分进行处理
                            old_score = Scores.objects.get(owner=target_user)

                        except Scores.DoesNotExist:
                            #新用户，创建
                            new_score = Scores(owner=target_user,score=entry.score)
                            new_score.save()
                            return HttpResponseRedirect(reverse('check:users'))

                        else:
                            #老用户，更新
                            old_score.score += float(entry.score)
                            old_score.save()

                            return HttpResponseRedirect(reverse('check:users'))

                    else:
                        messages.error(request, '不能给自己积分')
                        return HttpResponseRedirect(reverse('check:users'))

                    
       
    else:
        return Send403(request)