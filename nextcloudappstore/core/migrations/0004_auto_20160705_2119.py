# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-05 21:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_remove_app_recommendations'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'ordering': ['id'], 'verbose_name': 'Category', 'verbose_name_plural': 'Categories'},
        ),
        migrations.AddField(
            model_name='apptranslation',
            name='summary',
            field=models.CharField(default='', help_text="Short text describing the app's purpose", max_length=128, verbose_name='Summary'),
            preserve_default=False,
        ),
    ]