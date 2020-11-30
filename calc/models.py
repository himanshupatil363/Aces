from django.db import models
from django.contrib.auth.models import User
from django.forms import ModelChoiceField
from django import forms
from datetime import datetime, timedelta
from pprint import pprint

class extendUser(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    m_num = models.BigIntegerField()
    year = models.CharField(max_length=50)
    s_id = models.BigIntegerField()
    def __str__(self):
        return self.user.firstname    
# class exam(models.Model):
#     subject_name = models.CharField(max_length=100)
#     class_name = models.CharField(max_length=100)
#     department = models.CharField(max_length=100)
#     year = models.CharField(max_length=50)
#     sem = models.CharField(max_length=100)
# def __str__(self):
#         return self.class_name
class year(models.Model):
    yr = models.CharField(max_length=100)
    def __str__(self):
        return self.yr

class semester(models.Model):
    year = models.ForeignKey(year, on_delete=models.CASCADE)
    sem = models.CharField(max_length=50)
    def __str__(self):
        return self.sem

class subject(models.Model):
    sub_code = models.CharField(max_length=100)
    sub_name = models.CharField(max_length=100)
    year = models.ForeignKey(year, on_delete=models.CASCADE,null=True)
    semester = models.ForeignKey(semester, on_delete=models.CASCADE,null=True)
    def __str__(self):
        return self.sub_name
