# -*- coding: utf-8 -*-
# Generated by Django 1.9.9 on 2016-08-26 13:22
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_employeelisting_post_resume_or_cover'),
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('employee_name', models.CharField(max_length=50)),
                ('dob', models.DateField(max_length=8)),
                ('address', models.TextField()),
                ('telephone_number', models.IntegerField(unique=True, validators=[django.core.validators.RegexValidator(code='Invalid number', message='Length has to be 10', regex='^\\d{10}$')])),
                ('federal_and_state_filling_status', models.CharField(max_length=30)),
                ('department', models.CharField(max_length=50)),
                ('start_date', models.DateField(max_length=8)),
                ('end_date', models.DateField(max_length=8)),
                ('recieved_employee_handbook', models.BooleanField(default=True)),
                ('personel_notes', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='WorkSkills',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('appearence', models.IntegerField()),
                ('customer_skills', models.IntegerField()),
                ('team_work', models.IntegerField()),
                ('adhere_company_policies', models.IntegerField()),
                ('accepts_coaching', models.IntegerField()),
                ('self_starting', models.IntegerField()),
                ('employee_name', models.CharField(max_length=50)),
                ('employee_number', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Employee')),
            ],
        ),
    ]
