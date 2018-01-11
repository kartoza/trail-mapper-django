# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trail', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='poi',
            old_name='geometry',
            new_name='geom',
        ),
        migrations.RenameField(
            model_name='trail',
            old_name='geometry',
            new_name='geom',
        ),
        migrations.RenameField(
            model_name='trailsection',
            old_name='geometry',
            new_name='geom',
        ),
    ]
