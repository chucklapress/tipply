# -*- coding: utf-8 -*-
# Generated by Django 1.9.9 on 2016-09-11 21:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0009_employeelisting_applicant_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employeelisting',
            name='applicant_image',
            field=models.FileField(blank=True, null=True, upload_to='static/images'),
        ),
    ]