# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-09-01 20:38
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20160901_1408'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='avatar',
            field=models.ImageField(default='', upload_to='avatars', verbose_name='Аватар'),
            preserve_default=False,
        ),
    ]
