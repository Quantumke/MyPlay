# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Dplay',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=100)),
                ('thumbnail', models.CharField(max_length=100)),
                ('video', models.CharField(max_length=100)),
                ('uploaded_by', models.CharField(max_length=100)),
                ('date', models.DateField(max_length=100)),
                ('views', models.CharField(max_length=100)),
                ('category', models.CharField(max_length=100)),
                ('channel', models.CharField(max_length=100)),
            ],
        ),
    ]
