# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2018-03-01 18:21
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import django.db.models.manager


class Migration(migrations.Migration):

    dependencies = [
        ('cases', '0007_auto_20180222_0010'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='products',
            options={'ordering': ['name'], 'verbose_name': 'Produto', 'verbose_name_plural': 'Produtos'},
        ),
        migrations.AlterModelManagers(
            name='cases',
            managers=[
                ('object', django.db.models.manager.Manager()),
            ],
        ),
        migrations.AlterField(
            model_name='products',
            name='case',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='case', to='cases.Cases', verbose_name='Case'),
        ),
    ]