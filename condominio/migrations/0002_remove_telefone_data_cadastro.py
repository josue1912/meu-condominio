# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2016-12-17 19:14
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('condominio', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='telefone',
            name='data_cadastro',
        ),
    ]
