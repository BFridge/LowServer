# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Log',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('apkName', models.CharField(max_length=100)),
                ('methodName', models.CharField(max_length=100)),
                ('args', models.CharField(max_length=300)),
            ],
        ),
    ]
