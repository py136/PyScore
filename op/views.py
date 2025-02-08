from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required
def op_index(request):
    '''op主页（用于保护某些限制界面）'''
    user_groups = set(request.user.groups.all().values_list('name', flat=True))
    
    # 定义需要检查的组名
    required_groups = {'document_users', 'monitor_users', 'super_users'}
    
    # 检查当前用户是否属于任何一个必需的组
    if required_groups.intersection(user_groups):
        return render(request,'op/op_index.html')

    else:
        return render(request,'op/403.html')
