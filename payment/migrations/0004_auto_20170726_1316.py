# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-26 13:16
from __future__ import unicode_literals

from django.db import migrations, models
import payment.models


class Migration(migrations.Migration):

    dependencies = [
        ('payment', '0003_auto_20170725_1746'),
    ]

    operations = [
        migrations.CreateModel(
            name='Vendor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vendor_id', models.CharField(default=payment.models.uuidGenerator16, max_length=16, unique=True)),
                ('location', models.CharField(max_length=50)),
            ],
        ),
        migrations.AddField(
            model_name='product',
            name='slug',
            field=models.SlugField(default='slug'),
            preserve_default=False,
        ),
    ]