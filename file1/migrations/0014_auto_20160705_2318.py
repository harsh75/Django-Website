# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-07-05 17:48
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('file1', '0013_auto_20160705_2315'),
    ]

    operations = [
        migrations.CreateModel(
            name='ShareYourMemory2',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('memory_title', models.CharField(max_length=200, null=True)),
                ('memory_desription', models.CharField(max_length=200, null=True)),
                ('memory_images', models.FileField(null=True, upload_to='documents/%Y/%m/%d')),
                ('sharedM', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='file1.CategoryList')),
            ],
        ),
        migrations.RemoveField(
            model_name='shareyourmemory1',
            name='sharedM',
        ),
        migrations.DeleteModel(
            name='ShareYourMemory1',
        ),
    ]
