# coding: utf-8

from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class UserProfile(models.Model):
    GENDER_CHOICES = (
            ('M', '男'),
            ('F', '女'),
        )
    user = models.OneToOneField(User, verbose_name='用户的额外信息')
    fullname = models.CharField('姓名',max_length=80)
    gender = models.CharField('性别', max_length=1, choices=GENDER_CHOICES, default='M')
    tel = models.CharField('电话', max_length=20, blank=True)
    mobile = models.CharField('移动电话', max_length=20, blank=True)
    address = models.CharField('家庭地址', max_length=200, blank=True)
    QQ = models.CharField('QQ', max_length=50, blank=True)
    position = models.CharField('目前所在地', max_length=200, blank=True, default='北京')
    native = models.CharField('籍贯', max_length=50, blank=True,)

    def __unicode__(self):
        return self.fullname

