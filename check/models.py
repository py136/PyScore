from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class ScoreEntries(models.Model):
    '''存储用户积分细则'''
    text = models.TextField(max_length=100)
    date_added = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User,on_delete=models.CASCADE)
    score = models.IntegerField(default=0)      #用户的积分
    def __str__(self):
        '''返回SoreEntry'''
        return self.text
    
class Scores(models.Model):
    '''存储用户总得分'''
    score = models.IntegerField(default=0,db_index=True)
    owner = models.ForeignKey(User,on_delete=models.CASCADE)

    class Meta:
        # 联合索引：加速 ORDER BY -score, id 排序
        indexes = [
            models.Index(fields=['-score', 'id']),
        ]

    def __str__(self):
        return f"{self.owner.username}: {self.score}"