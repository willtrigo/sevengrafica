# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2018-02-14 18:10
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cases', '0003_auto_20180214_1809'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cases',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='sevengrafica/static/img/cases', verbose_name='Imagem'),
        ),
    ]
