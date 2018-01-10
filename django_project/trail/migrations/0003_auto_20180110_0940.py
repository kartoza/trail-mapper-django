# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trail', '0002_auto_20180110_0936'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='poi',
            options={'ordering': ['name'], 'verbose_name_plural': 'Points of Interest (POIs)'},
        ),
    ]
