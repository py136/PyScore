from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required
def CheckAuthority(request):
    '''检查用户权限'''

    user_groups = set(request.user.groups.all().values_list('name', flat=True))
    
    # 定义需要检查的组名
    required_groups = {'super_users'}
    
    # 检查当前用户是否属于任何一个必需的组
    if required_groups.intersection(user_groups) or request.user.is_superuser : 
        return True
    
    else:
        return False

@login_required
def Send403(request, op_required=False):
    '''用于发送403界面'''
    if op_required:
        #与OP界面适配
        return render(request, 'op/403_op.html')

    else:
        return render(request,'op/403.html')

@login_required
def CheckOwner(request,owner):
    '''检测当前请求是否属于该用户'''
    if request.user == owner:
        return True   #检测成功，返回
    else:
        return False