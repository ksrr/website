# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-01 15:04
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import images.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('register', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Folder',
            fields=[
                ('folder_name', models.CharField(max_length=50, primary_key=True, serialize=False, unique=True)),
                ('folder_description', models.CharField(max_length=200)),
                ('folder_type', models.CharField(choices=[(b'technical', b'Technical'), (b'fun', b'Fun'), (b'other', b'Other')], max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.ImageField(upload_to=images.models.content_file_name)),
                ('folder_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='images.Folder')),
            ],
        ),
        migrations.CreateModel(
            name='ProfileImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(storage=images.models.OverwriteStorage(), upload_to=b'images/profile_image/')),
                ('username', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='register.User_info')),
            ],
        ),
        migrations.AlterUniqueTogether(
            name='image',
            unique_together=set([('img', 'folder_name')]),
        ),
    ]