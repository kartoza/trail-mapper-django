# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trail_mapper', '0003_auto_20180112_1332'),
    ]

    operations = [
        migrations.RenameField(
            model_name='trailsection',
            old_name='grade_id',
            new_name='grade',
        ),
    ]
