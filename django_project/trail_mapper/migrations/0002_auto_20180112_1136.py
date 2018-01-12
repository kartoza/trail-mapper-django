# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.contrib.gis.db.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('trail_mapper', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trail',
            name='geom',
            field=django.contrib.gis.db.models.fields.PointField(srid=4326, dim=3, null=True, geography=True, blank=True),
        ),
        migrations.AlterField(
            model_name='trailsection',
            name='geom',
            field=django.contrib.gis.db.models.fields.LineStringField(srid=4326, dim=3, geography=True),
        ),
    ]
