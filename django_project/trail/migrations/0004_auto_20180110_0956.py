# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('trail', '0003_auto_20180110_0940'),
    ]

    operations = [
        migrations.AddField(
            model_name='trail',
            name='guid',
            field=models.UUIDField(default=uuid.uuid4, verbose_name='GUID', editable=False),
        ),
        migrations.AlterField(
            model_name='poi',
            name='trail_section',
            field=models.ForeignKey(to='trail.TrailSection'),
        ),
    ]
