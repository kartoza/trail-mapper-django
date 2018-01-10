# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('trail', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='trail',
            name='guid',
        ),
        migrations.AddField(
            model_name='grade',
            name='guid',
            field=models.UUIDField(default=uuid.uuid4, verbose_name='GUID', editable=False),
        ),
    ]
