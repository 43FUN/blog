# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from users.models import User
import datetime


# Create your models here.
class Article(models.Model):
    class Meta():
        db_table = 'article'
    article_title = models.CharField(
        'Название статьи', max_length = 200)
    article_text = models.TextField('Текст статьи')
    article_date = models.DateTimeField(
        default=datetime.datetime.now)
    article_likes = models.IntegerField(default=0)
    article_author = models.ForeignKey(User, verbose_name='Автор')


class Comments(models.Model):
    class Meta():
        db_table = 'comments'
    comments_text = models.TextField(verbose_name="Комментарий")
    comments_article = models.ForeignKey(Article)
    comments_author = models.ForeignKey(User, verbose_name='Автор')
    comments_date = models.DateTimeField(
        default=datetime.datetime.now)
