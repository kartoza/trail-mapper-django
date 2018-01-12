# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trail_mapper', '0002_auto_20180112_1136'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='POI',
            new_name='PointOfInterest',
        ),
    ]
