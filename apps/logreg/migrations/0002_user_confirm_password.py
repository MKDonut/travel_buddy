# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-15 22:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('logreg', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='confirm_password',
            field=models.CharField(default='SOME STRING', max_length=255),
        ),
    ]
