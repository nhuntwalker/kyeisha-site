# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-12-19 09:34
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='excerpt',
            field=models.TextField(blank=True, null=True),
        ),
    ]
