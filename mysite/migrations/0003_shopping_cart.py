# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2018-02-19 19:03
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0002_auto_20180219_1806'),
    ]

    operations = [
        migrations.CreateModel(
            name='Shopping_Cart',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('isbn', models.IntegerField()),
                ('author', models.CharField(max_length=25)),
                ('price', models.DecimalField(decimal_places=2, max_digits=7)),
            ],
        ),
    ]
