# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-04-07 14:30
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('microb', '0004_auto_20180407_1429'),
    ]

    operations = [
        migrations.AlterField(
            model_name='instance',
            name='port',
            field=models.PositiveIntegerField(blank=True, null=True, verbose_name='Port'),
        ),
    ]
