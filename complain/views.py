from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import ComplainDetails
from check.models import ScoreEntries
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.urls import reverse
from op.authority import CheckAuthority,Send403
from check.models import ScoreEntries,Scores
from op.authority import CheckOwner,Send403

# Create your views here.

@login_required
def ComplainDetail(request,entry_id):
    '''用于用户申诉'''
    entry = ScoreEntries.objects.get(id=entry_id)
    if CheckOwner(request,entry.owner):
        #检查通过，进行操作
        if request.method != 'POST':
            #发送申诉表单
            context = {'entry':entry}
            return render(request,'complain/complain_detail.html',context)
        
        else:
            #对数据进行处理
            if len(request.POST.get('reason')) > 100:
                #过滤长输入
                messages.error(request,'输入字符长度超过100字')
                return HttpResponseRedirect(reverse('complain:complain_detail',args=[entry.id]))
            
            elif len(request.POST.get('reason')) <= 100:
                #对输入进行处理
                detail = ComplainDetails(detailid=entry.id,owner=entry.owner,reason=request.POST.get('reason'))
                detail.save()
                return HttpResponseRedirect(reverse('check:entry'))

    else:
        return Send403(request)
        
@login_required
def DealComplain(request,complaint_id):
    '''处理申诉项目'''
    #检查用户权限

    reason = ComplainDetails.objects.get(id=complaint_id)     #获取申诉原因，用于后续权限检查
    if CheckAuthority(request) and not CheckOwner(request, reason.owner):
        #判断操作
        if request.method != 'POST':
            #发送页面
            try:
                #保护，防止重复出现申诉条目
                entry = ScoreEntries.objects.get(id=reason.detailid)

            except ScoreEntries.DoesNotExist:
                reason.delete()
                messages.error(request,'条目已处理完毕')
                return HttpResponseRedirect(reverse('check:complaints'))
            

            else:
                context = {'entry':entry,'complaint':reason}
                return render(request,'complain/deal_complain.html',context)
        
        else:
            #对提交的申诉进行处理

            userreason = ComplainDetails.objects.get(id=complaint_id)
            if request.POST.get('deal') == 'yes':
                #同意，撤销积分

                try:
                    #保护，防止重复出现申诉条目
                    userentry = ScoreEntries.objects.get(id=userreason.detailid)

                except ScoreEntries.DoesNotExist:
                    userreason.delete()
                    return HttpResponseRedirect(reverse('check:complaints'))
                
                else:
                    userscore = Scores.objects.get(owner=userreason.owner)

                    userscore.score -= userentry.score     #更新积分
                    userentry.delete()                
                    userreason.delete()
                    userscore.save()         #保存更改

                    return HttpResponseRedirect(reverse('check:complaints'))
            
            else:
                userreason.delete()
                return HttpResponseRedirect(reverse('check:complaints'))
                
    else:
        return Send403(request)
    
@login_required
def DeleteScore(request,entry_id):
    '''用于管理员删除积分条目'''
    #检查用户权限
    if CheckAuthority(request):
        entry = ScoreEntries.objects.get(id=entry_id)
        if request.method != 'POST':
            #发送确认表单
            context = {'entry':entry}
            return render(request,'complain/delete_score.html',context)
        
        else:
            #确认后，对相应积分进行删除
            userscore = Scores.objects.get(owner=entry.owner)
            userscore.score -= entry.score      #对积分进行更新
            userscore.save()
            entry.delete()
            messages.error(request,'积分删除完毕')
            return HttpResponseRedirect(reverse('check:details',args=[userscore.owner.username]))

    else:
        return Send403(request)