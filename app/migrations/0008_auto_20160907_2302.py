# -*- coding: utf-8 -*-
# Generated by Django 1.9.9 on 2016-09-07 23:02
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_book'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employeelisting',
            name='applicant_phone',
            field=models.IntegerField(),
        ),
    ]
