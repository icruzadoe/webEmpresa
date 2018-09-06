# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('tittle', models.CharField(verbose_name='Título', max_length=200)),
                ('subtitle', models.CharField(verbose_name='SubTítulo', max_length=200)),
                ('content', models.TextField(verbose_name='Contenido')),
                ('image', models.ImageField(verbose_name='Imagen', upload_to='services')),
                ('created', models.DateTimeField(verbose_name='Fecha de creación', auto_now_add=True)),
                ('updated', models.DateTimeField(verbose_name='Fecha de actualización', auto_now=True)),
            ],
            options={
                'verbose_name': 'servicio',
                'verbose_name_plural': 'servicios',
                'ordering': ['-created'],
            },
        ),
    ]
