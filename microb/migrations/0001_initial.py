# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-04-17 07:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Instance',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('domain', models.CharField(max_length=120, unique=True, verbose_name='Domain')),
                ('ip', models.GenericIPAddressField(blank=True, null=True, unique=True, verbose_name='Ip adress')),
                ('port', models.PositiveIntegerField(blank=True, null=True, verbose_name='Port')),
                ('url', models.URLField(blank=True)),
                ('channel_in', models.CharField(blank=True, max_length=120)),
                ('channel_out', models.CharField(blank=True, max_length=120)),
            ],
            options={
                'verbose_name_plural': 'Instances',
                'verbose_name': 'Instance',
                'ordering': ('domain', 'ip'),
            },
        ),
        migrations.AlterUniqueTogether(
            name='instance',
            unique_together=set([('domain', 'ip')]),
        ),
    ]
