# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50, verbose_name='name')),
                ('old', models.PositiveIntegerField(verbose_name='name')),
                ('content', models.CharField(default=None, max_length=2, verbose_name='contents', choices=[('1', 'test1'), ('2', 'test2'), ('3', 'test3')])),
            ],
        ),
    ]
