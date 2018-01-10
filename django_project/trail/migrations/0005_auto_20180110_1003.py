# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('trail', '0004_auto_20180110_0956'),
    ]

    operations = [
        migrations.AddField(
            model_name='poi',
            name='guid',
            field=models.UUIDField(default=uuid.uuid4, verbose_name='GUID', editable=False),
        ),
        migrations.AddField(
            model_name='trailsection',
            name='guid',
            field=models.UUIDField(default=uuid.uuid4, verbose_name='GUID', editable=False),
        ),
    ]
