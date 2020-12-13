from django.db import models
from django.contrib.auth.models import User
from django.forms import ModelChoiceField
from django import forms
from datetime import datetime, timedelta
from pprint import pprint

class dffem(models.Model):
    que = models.CharField(max_length=1000)
    op1 = models.CharField(max_length=400)
    op2 = models.CharField(max_length=400)
    op3 = models.CharField(max_length=400)
    op4 = models.CharField(max_length=400)
    ans = models.CharField(max_length=400)
    category = models.CharField(max_length=200)
    def __str__(self):
        return self.que

class dffec(models.Model):
    que = models.CharField(max_length=1000)
    op1 = models.CharField(max_length=400)
    op2 = models.CharField(max_length=400)
    op3 = models.CharField(max_length=400)
    op4 = models.CharField(max_length=400)
    ans = models.CharField(max_length=400)
    category = models.CharField(max_length=200)
    def __str__(self):
        return self.que

class dffemh(models.Model):
    que = models.CharField(max_length=1000)
    op1 = models.CharField(max_length=400)
    op2 = models.CharField(max_length=400)
    op3 = models.CharField(max_length=400)
    op4 = models.CharField(max_length=400)
    ans = models.CharField(max_length=400)
    category = models.CharField(max_length=200)
    def __str__(self):
        return self.que


class dffcp(models.Model):
    que = models.CharField(max_length=1000)
    op1 = models.CharField(max_length=400)
    op2 = models.CharField(max_length=400)
    op3 = models.CharField(max_length=400)
    op4 = models.CharField(max_length=400)
    ans = models.CharField(max_length=400)
    category = models.CharField(max_length=200)
    def __str__(self):
        return self.que

class dfsem(models.Model):
    que = models.CharField(max_length=1000)
    op1 = models.CharField(max_length=400)
    op2 = models.CharField(max_length=400)
    op3 = models.CharField(max_length=400)
    op4 = models.CharField(max_length=400)
    ans = models.CharField(max_length=400)
    category = models.CharField(max_length=200)
    def __str__(self):
        return self.que

class dfsep(models.Model):
    que = models.CharField(max_length=1000)
    op1 = models.CharField(max_length=400)
    op2 = models.CharField(max_length=400)
    op3 = models.CharField(max_length=400)
    op4 = models.CharField(max_length=400)
    ans = models.CharField(max_length=400)
    category = models.CharField(max_length=200)
    def __str__(self):
        return self.que

class dfseg(models.Model):
    que = models.CharField(max_length=1000)
    op1 = models.CharField(max_length=400)
    op2 = models.CharField(max_length=400)
    op3 = models.CharField(max_length=400)
    op4 = models.CharField(max_length=400)
    ans = models.CharField(max_length=400)
    category = models.CharField(max_length=200)
    def __str__(self):
        return self.que

class dfscs(models.Model):
    que = models.CharField(max_length=1000)
    op1 = models.CharField(max_length=400)
    op2 = models.CharField(max_length=400)
    op3 = models.CharField(max_length=400)
    op4 = models.CharField(max_length=400)
    ans = models.CharField(max_length=400)
    category = models.CharField(max_length=200)
    def __str__(self):
        return self.que

class dstem(models.Model):
    que = models.CharField(max_length=1000)
    op1 = models.CharField(max_length=400)
    op2 = models.CharField(max_length=400)
    op3 = models.CharField(max_length=400)
    op4 = models.CharField(max_length=400)
    ans = models.CharField(max_length=400)
    category = models.CharField(max_length=200)
    def __str__(self):
        return self.que

class dstdm(models.Model):
    que = models.CharField(max_length=1000)
    op1 = models.CharField(max_length=400)
    op2 = models.CharField(max_length=400)
    op3 = models.CharField(max_length=400)
    op4 = models.CharField(max_length=400)
    ans = models.CharField(max_length=400)
    category = models.CharField(max_length=200)
    def __str__(self):
        return self.que

class dstds(models.Model):
    que = models.CharField(max_length=1000)
    op1 = models.CharField(max_length=400)
    op2 = models.CharField(max_length=400)
    op3 = models.CharField(max_length=400)
    op4 = models.CharField(max_length=400)
    ans = models.CharField(max_length=400)
    category = models.CharField(max_length=200)
    def __str__(self):
        return self.que

class dstca(models.Model):
    que = models.CharField(max_length=1000)
    op1 = models.CharField(max_length=400)
    op2 = models.CharField(max_length=400)
    op3 = models.CharField(max_length=400)
    op4 = models.CharField(max_length=400)
    ans = models.CharField(max_length=400)
    category = models.CharField(max_length=200)
    def __str__(self):
        return self.que

class dsfda(models.Model):
    que = models.CharField(max_length=1000)
    op1 = models.CharField(max_length=400)
    op2 = models.CharField(max_length=400)
    op3 = models.CharField(max_length=400)
    op4 = models.CharField(max_length=400)
    ans = models.CharField(max_length=400)
    category = models.CharField(max_length=200)
    def __str__(self):
        return self.que

class dsfps(models.Model):
    que = models.CharField(max_length=1000)
    op1 = models.CharField(max_length=400)
    op2 = models.CharField(max_length=400)
    op3 = models.CharField(max_length=400)
    op4 = models.CharField(max_length=400)
    ans = models.CharField(max_length=400)
    category = models.CharField(max_length=200)
    def __str__(self):
        return self.que

class dsfos(models.Model):
    que = models.CharField(max_length=1000)
    op1 = models.CharField(max_length=400)
    op2 = models.CharField(max_length=400)
    op3 = models.CharField(max_length=400)
    op4 = models.CharField(max_length=400)
    ans = models.CharField(max_length=400)
    category = models.CharField(max_length=200)
    def __str__(self):
        return self.que

class dsfpd(models.Model):
    que = models.CharField(max_length=1000)
    op1 = models.CharField(max_length=400)
    op2 = models.CharField(max_length=400)
    op3 = models.CharField(max_length=400)
    op4 = models.CharField(max_length=400)
    ans = models.CharField(max_length=400)
    category = models.CharField(max_length=200)
    def __str__(self):
        return self.que

class dtfds(models.Model):
    que = models.CharField(max_length=1000)
    op1 = models.CharField(max_length=400)
    op2 = models.CharField(max_length=400)
    op3 = models.CharField(max_length=400)
    op4 = models.CharField(max_length=400)
    ans = models.CharField(max_length=400)
    category = models.CharField(max_length=200)
    def __str__(self):
        return self.que

class dtftc(models.Model):
    que = models.CharField(max_length=1000)
    op1 = models.CharField(max_length=400)
    op2 = models.CharField(max_length=400)
    op3 = models.CharField(max_length=400)
    op4 = models.CharField(max_length=400)
    ans = models.CharField(max_length=400)
    category = models.CharField(max_length=200)
    def __str__(self):
        return self.que

class dtfml(models.Model):
    que = models.CharField(max_length=1000)
    op1 = models.CharField(max_length=400)
    op2 = models.CharField(max_length=400)
    op3 = models.CharField(max_length=400)
    op4 = models.CharField(max_length=400)
    ans = models.CharField(max_length=400)
    category = models.CharField(max_length=200)
    def __str__(self):
        return self.que

class dtfcl(models.Model):
    que = models.CharField(max_length=1000)
    op1 = models.CharField(max_length=400)
    op2 = models.CharField(max_length=400)
    op3 = models.CharField(max_length=400)
    op4 = models.CharField(max_length=400)
    ans = models.CharField(max_length=400)
    category = models.CharField(max_length=200)
    def __str__(self):
        return self.que

class dtscd(models.Model):
    que = models.CharField(max_length=1000)
    op1 = models.CharField(max_length=400)
    op2 = models.CharField(max_length=400)
    op3 = models.CharField(max_length=400)
    op4 = models.CharField(max_length=400)
    ans = models.CharField(max_length=400)
    category = models.CharField(max_length=200)
    def __str__(self):
        return self.que

class dtscn(models.Model):
    que = models.CharField(max_length=1000)
    op1 = models.CharField(max_length=400)
    op2 = models.CharField(max_length=400)
    op3 = models.CharField(max_length=400)
    op4 = models.CharField(max_length=400)
    ans = models.CharField(max_length=400)
    category = models.CharField(max_length=200)
    def __str__(self):
        return self.que

class dtsai(models.Model):
    que = models.CharField(max_length=1000)
    op1 = models.CharField(max_length=400)
    op2 = models.CharField(max_length=400)
    op3 = models.CharField(max_length=400)
    op4 = models.CharField(max_length=400)
    ans = models.CharField(max_length=400)
    category = models.CharField(max_length=200)
    def __str__(self):
        return self.que

class dtsiot(models.Model):
    que = models.CharField(max_length=1000)
    op1 = models.CharField(max_length=400)
    op2 = models.CharField(max_length=400)
    op3 = models.CharField(max_length=400)
    op4 = models.CharField(max_length=400)
    ans = models.CharField(max_length=400)
    category = models.CharField(max_length=200)
    def __str__(self):
        return self.que

class dfsvse(models.Model):
    que = models.CharField(max_length=1000)
    op1 = models.CharField(max_length=400)
    op2 = models.CharField(max_length=400)
    op3 = models.CharField(max_length=400)
    op4 = models.CharField(max_length=400)
    ans = models.CharField(max_length=400)
    category = models.CharField(max_length=200)
    def __str__(self):
        return self.que

class dfsvds(models.Model):
    que = models.CharField(max_length=1000)
    op1 = models.CharField(max_length=400)
    op2 = models.CharField(max_length=400)
    op3 = models.CharField(max_length=400)
    op4 = models.CharField(max_length=400)
    ans = models.CharField(max_length=400)
    category = models.CharField(max_length=200)
    def __str__(self):
        return self.que

class dfsvcc(models.Model):
    que = models.CharField(max_length=1000)
    op1 = models.CharField(max_length=400)
    op2 = models.CharField(max_length=400)
    op3 = models.CharField(max_length=400)
    op4 = models.CharField(max_length=400)
    ans = models.CharField(max_length=400)
    category = models.CharField(max_length=200)
    def __str__(self):
        return self.que

class dfsvbt(models.Model):
    que = models.CharField(max_length=1000)
    op1 = models.CharField(max_length=400)
    op2 = models.CharField(max_length=400)
    op3 = models.CharField(max_length=400)
    op4 = models.CharField(max_length=400)
    ans = models.CharField(max_length=400)
    category = models.CharField(max_length=200)
    def __str__(self):
        return self.que

class dfegdp(models.Model):
    que = models.CharField(max_length=1000)
    op1 = models.CharField(max_length=400)
    op2 = models.CharField(max_length=400)
    op3 = models.CharField(max_length=400)
    op4 = models.CharField(max_length=400)
    ans = models.CharField(max_length=400)
    category = models.CharField(max_length=200)
    def __str__(self):
        return self.que

class dfegcn(models.Model):
    que = models.CharField(max_length=1000)
    op1 = models.CharField(max_length=400)
    op2 = models.CharField(max_length=400)
    op3 = models.CharField(max_length=400)
    op4 = models.CharField(max_length=400)
    ans = models.CharField(max_length=400)
    category = models.CharField(max_length=200)
    def __str__(self):
        return self.que