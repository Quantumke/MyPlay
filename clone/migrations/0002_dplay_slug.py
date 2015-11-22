# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('clone', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='dplay',
            name='slug',
            field=models.SlugField(default=datetime.datetime(2015, 11, 22, 14, 48, 33, 974629, tzinfo=utc), unique=True, max_length=100),
            preserve_default=False,
        ),
    ]
