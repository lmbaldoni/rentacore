# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-06-07 20:01
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profitability', '0008_auto_20170607_1104'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='album',
            name='album_id',
        ),
        migrations.AddField(
            model_name='album',
            name='id',
            field=models.AutoField(auto_created=True, default=1, primary_key=True, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='userprofile',
            name='user2',
            field=models.IntegerField(default=1, primary_key=True),
            preserve_default=False,
        ),
    ]
