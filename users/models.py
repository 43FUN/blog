#-*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.


class User(AbstractUser):
    avatar = models.ImageField('Аватар', upload_to='avatars')
    phone = models.CharField('Телефон', max_length=20)
    skype = models.CharField('Skype', max_length=50)


