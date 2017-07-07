# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-26 02:25
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Members',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_code', models.IntegerField(default=0)),
                ('id_alfa', models.CharField(blank=True, default='', max_length=20)),
                ('name', models.CharField(blank=True, default='', max_length=20)),
                ('description', models.CharField(blank=True, default='', max_length=100)),
                ('enabled', models.BooleanField(default=False)),
                ('if_lead', models.BooleanField(default=False)),
                ('create_date', models.DateTimeField(auto_now_add=True)),
                ('create_by', models.CharField(max_length=20)),
                ('modified_date', models.DateTimeField(auto_now_add=True)),
                ('modified_by', models.CharField(max_length=20)),
            ],
            options={
                'ordering': ('id_code',),
            },
        ),
    ]
