# -*- coding: utf-8 -*-
# Generated by Django 1.9.9 on 2016-09-12 00:15
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0012_auto_20160911_2230'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employeelisting',
            name='applicant_image',
            field=models.FileField(blank=True, null=True, upload_to='/app/static/images'),
        ),
    ]
