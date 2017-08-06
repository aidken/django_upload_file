# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-05 09:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='file',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file_name', models.CharField(max_length=200)),
                ('upload_datetime', models.DateTimeField(verbose_name='Date uploaded.')),
                ('comment', models.CharField(max_length=5000)),
            ],
        ),
    ]
