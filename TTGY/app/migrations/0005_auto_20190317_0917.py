# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2019-03-17 09:17
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_auto_20190316_0321'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='password',
            new_name='t_password',
        ),
        migrations.RenameField(
            model_name='user',
            old_name='phone_num',
            new_name='t_phone',
        ),
        migrations.AlterField(
            model_name='user',
            name='token',
            field=models.CharField(max_length=256),
        ),
    ]
