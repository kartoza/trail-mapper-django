# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trail', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='grade',
            name='guid',
        ),
        migrations.RemoveField(
            model_name='poi',
            name='guid',
        ),
        migrations.RemoveField(
            model_name='trailsection',
            name='guid',
        ),
    ]
