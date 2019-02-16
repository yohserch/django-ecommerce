# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-02-16 06:58
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0008_auto_20190216_0512'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='timestamp',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
