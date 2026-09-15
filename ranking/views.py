from django.shortcuts import render
from django.core.paginator import Paginator
from django.views.decorators.cache import cache_page
from django.http import JsonResponse
from check.models import Scores

@cache_page(60 * 5)
def leaderboard(request):
    scores_list = Scores.objects.select_related('owner') \
                    .only('owner__username', 'score') \
                    .order_by('-score', 'id')
    
    paginator = Paginator(scores_list, 20)
    page_number = request.GET.get('page', 1)
    page_obj = paginator.get_page(page_number)
    
    start_index = (page_obj.number - 1) * paginator.per_page
    for idx, score in enumerate(page_obj, start=1):
        score.rank = start_index + idx
    
    return render(request, 'ranking/leaderboard.html', {'page_obj': page_obj})

def my_rank_api(request):
    # 直接处理 JSON 响应
    if not request.user.is_authenticated:
        return JsonResponse({'error': '请先登录'}, status=401)
    
    try:
        user_score = Scores.objects.get(owner=request.user)
        rank = Scores.objects.filter(score__gt=user_score.score).count() + 1
        return JsonResponse({
            'score': user_score.score,
            'rank': rank,
        })
    except Scores.DoesNotExist:
        return JsonResponse({
            'error': '您还没有积分记录',
            'score': 0,
            'rank': '未上榜'
        }, status=404)