# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trail', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trail',
            name='offset',
            field=models.CharField(help_text='Enter offset value i.e -2', max_length=255, null=True, verbose_name='Offset', blank=True),
        ),
    ]
