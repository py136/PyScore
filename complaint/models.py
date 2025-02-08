from django.db import models
from django.contrib.auth.models import User

class Complaint_Score_Details(models.Model):
    '''用来存储用户申诉条目'''
    score = models.IntegerField(default = 0)
    text = models.TextField(max_length = 50)
    date_added = models.DateTimeField(auto_now_add = True)
    owner = models.ForeignKey(User,on_delete = models.CASCADE)
    original_id = models.IntegerField(default = 0)
    state = models.TextField(max_length = 3)
    reason = models.TextField(max_length = 100)
    sign = models.TextField(max_length = 50)

    def __str__(self):
        '''返回text'''
        return self.text
    
    class Meta:
        verbose_name_plural = 'complaint_score_details'

class Complaint_Score_Details_History(models.Model):
    '''用来存储用户申诉过的条目'''
    score = models.IntegerField(default = 0)
    text = models.TextField(max_length = 50)
    date_added = models.DateTimeField(auto_now_add = True)
    owner = models.ForeignKey(User,on_delete = models.CASCADE)
    reason = models.TextField(max_length = 100)
    state = models.TextField(max_length = 3)

    def __str__(self):
        '''返回text'''
        return self.text
    
    class Meta:
        verbose_name_plural = 'complaint_score_details_history'


class Complaint_Score_Details_History_User(models.Model):
    '''用来存储用户申诉过的条目（用户查看）'''
    score = models.IntegerField(default = 0)
    text = models.TextField(max_length = 50)
    date_added = models.DateTimeField(auto_now_add = True)
    owner = models.ForeignKey(User,on_delete = models.CASCADE)
    state = models.TextField(max_length = 3)
    reason = models.TextField(max_length = 100)
    sign = models.TextField(max_length = 50)

    def __str__(self):
        '''返回text'''
        return self.text
    
    class Meta:
        verbose_name_plural = 'complaint_score_details_history_user'