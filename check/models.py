from django.db import models
from django.contrib.auth.models import User


class Score_Topics(models.Model):
    '''用来储存用户积分详情'''
    text = models.TextField(max_length = 20)
    date_added = models.DateTimeField(auto_now_add = True)
    owner = models.ForeignKey(User,on_delete = models.CASCADE)

    def __str__(self):
        '''返回Score_Topics'''
        return self.text
    
class Score_all(models.Model):
    '''用于储存此用户本周所有积分情况'''
    score = models.IntegerField(default = 0)
    text = models.TextField(max_length = 50)
    date_added = models.DateTimeField(auto_now_add = True)
    topic = models.ForeignKey(Score_Topics,on_delete = models.CASCADE)
    owner = models.ForeignKey(User,on_delete = models.CASCADE)

    class Meta:
        verbose_name_plural = 'score_all'

    def __str__(self):
        '''返回Sore'''
        return self.text

class Scores_Histories(models.Model):
    '''用户的积分历史'''
    score = models.IntegerField(default = 0)
    text = models.TextField(max_length = 50)
    date_added = models.DateTimeField(auto_now_add = True)
    owner = models.ForeignKey(User,on_delete = models.CASCADE)

    class Meta:
        verbose_name_plural = 'scores_histories'

    def __str__(self):
        '''返回Sore'''
        return self.text