from django.db import models
from django.contrib.auth.models import User

class Ranking_Scores(models.Model):
    '''存储用户的最终积分'''
    score = models.PositiveIntegerField(default=0)
    owner = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        '''返回分数'''
        return f"Score: {self.score}"


