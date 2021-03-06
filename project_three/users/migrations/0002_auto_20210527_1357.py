# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2021-05-27 13:57
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=264, unique=True)),
                ('last_name', models.CharField(max_length=264)),
                ('email', models.EmailField(max_length=264)),
            ],
        ),
        migrations.RemoveField(
            model_name='emailaddress',
            name='name',
        ),
        migrations.RemoveField(
            model_name='lastname',
            name='name',
        ),
        migrations.DeleteModel(
            name='EmailAddress',
        ),
        migrations.DeleteModel(
            name='FirstName',
        ),
        migrations.DeleteModel(
            name='LastName',
        ),
    ]
