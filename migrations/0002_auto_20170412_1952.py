# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-04-13 00:52
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('seniorprojectapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='first_name',
            field=models.CharField(max_length=50, validators=[django.core.validators.RegexValidator('^[a-zA-Z]*$', 'Only alphabetic characters allowed')]),
        ),
        migrations.AlterField(
            model_name='user',
            name='last_name',
            field=models.CharField(max_length=50, validators=[django.core.validators.RegexValidator('^[a-zA-Z]*$', 'Only alphabetic characters allowed')]),
        ),
        migrations.AlterField(
            model_name='user',
            name='password',
            field=models.CharField(max_length=20, validators=[django.core.validators.MinLengthValidator(8, 'Your password must contain at least 8 characters.')]),
        ),
        migrations.AlterField(
            model_name='user',
            name='user_email',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='user',
            name='user_name',
            field=models.CharField(max_length=50),
        ),
    ]