# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-10 06:33
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('register', '0005_auto_20170210_1124'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='username',
        ),
        migrations.DeleteModel(
            name='Student',
        ),
    ]