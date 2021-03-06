# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-29 16:23
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('payment', '0002_auto_20170729_1315'),
    ]

    operations = [
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('prepaid_card', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='payment.PrepaidCard')),
                ('user_card', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='payment.UserCard')),
            ],
            options={
                'get_latest_by': 'date',
            },
        ),
    ]
