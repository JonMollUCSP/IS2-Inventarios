# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-07 21:38
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aplicacion', '0007_auto_20170506_1434'),
    ]

    operations = [
        migrations.RenameField(
            model_name='proveedor',
            old_name='email',
            new_name='correo',
        ),
        migrations.RenameField(
            model_name='usuario',
            old_name='email',
            new_name='correo',
        ),
        migrations.AlterField(
            model_name='almacen',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
