# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trail', '0003_auto_20180110_0856'),
    ]

    operations = [
        migrations.CreateModel(
            name='TrailSections',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('order', models.CharField(help_text='Enter ordering of trail sections.', max_length=255, verbose_name='Order')),
                ('slug', models.SlugField()),
                ('trail', models.ForeignKey(to='trail.Trail')),
            ],
            options={
                'ordering': ['order'],
                'verbose_name_plural': 'Trail Sections',
            },
        ),
        migrations.AlterModelOptions(
            name='trailsection',
            options={'ordering': ['name'], 'verbose_name_plural': 'Trail Section'},
        ),
        migrations.AddField(
            model_name='trailsections',
            name='trail_section',
            field=models.ForeignKey(to='trail.TrailSection'),
        ),
    ]
