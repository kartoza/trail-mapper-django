# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import uuid
import django.contrib.gis.db.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('trail', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='grade',
            options={'ordering': ['name']},
        ),
        migrations.AlterModelOptions(
            name='trail',
            options={},
        ),
        migrations.AlterModelOptions(
            name='trailsection',
            options={'verbose_name_plural': 'Trail Section'},
        ),
        migrations.RemoveField(
            model_name='category',
            name='geometry',
        ),
        migrations.AddField(
            model_name='poi',
            name='geometry',
            field=django.contrib.gis.db.models.fields.PointField(srid=4326, null=True, geography=True, blank=True),
        ),
        migrations.AlterField(
            model_name='category',
            name='guid',
            field=models.UUIDField(default=uuid.uuid4, verbose_name='GUID', editable=False),
        ),
        migrations.AlterField(
            model_name='trail',
            name='geometry',
            field=django.contrib.gis.db.models.fields.PointField(srid=4326, null=True, geography=True, blank=True),
        ),
        migrations.AlterField(
            model_name='trailsection',
            name='geometry',
            field=django.contrib.gis.db.models.fields.PointField(srid=4326),
        ),
        migrations.AlterUniqueTogether(
            name='trail',
            unique_together=set([]),
        ),
        migrations.AlterUniqueTogether(
            name='trailsection',
            unique_together=set([]),
        ),
    ]
