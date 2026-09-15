from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class ComplainDetails(models.Model):
    '''用于存储用户申诉条目'''
    detailid = models.IntegerField(default=0)
    reason = models.TextField(max_length=100)
    owner = models.ForeignKey(User,on_delete=models.CASCADE)

    def __str__(self):
        '''返回id'''
        return str(self.owner.username)