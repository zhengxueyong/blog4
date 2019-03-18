# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2019-03-15 06:34
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Goods',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('icon', models.CharField(max_length=255)),
                ('price', models.IntegerField()),
                ('detail', models.CharField(max_length=255)),
            ],
            options={
                'db_table': 'goods',
            },
        ),
    ]
