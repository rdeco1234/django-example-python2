# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_auto_20180129_0639'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.IntegerField(serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=254)),
                ('message', models.TextField()),
                ('datetime', models.DateTimeField()),
            ],
        ),
        migrations.DeleteModel(
            name='Author',
        ),
    ]
