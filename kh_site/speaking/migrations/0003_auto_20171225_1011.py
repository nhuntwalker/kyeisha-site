# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-12-25 10:11
from __future__ import unicode_literals

from django.db import migrations
import redactor.fields


class Migration(migrations.Migration):

    dependencies = [
        ('speaking', '0002_presentation_subtitle'),
    ]

    operations = [
        migrations.AlterField(
            model_name='presentation',
            name='details',
            field=redactor.fields.RedactorField(blank=True, null=True),
        ),
    ]
