# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.contrib.gis.db.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('trail', '0002_auto_20180110_0849'),
    ]

    operations = [
        migrations.CreateModel(
            name='Grade',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(help_text='Enter Grade name of the Trail.', max_length=255, verbose_name='Grade Name')),
                ('image', models.ImageField(help_text='An image of the trail grade. Most browsers support dragging the image directly on to the "Choose File" button above.', upload_to=b'images/trail_grade', null=True, verbose_name='Image file', blank=True)),
                ('slug', models.SlugField()),
            ],
            options={
                'ordering': ['name'],
                'verbose_name_plural': 'Grades',
            },
        ),
        migrations.CreateModel(
            name='TrailSection',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(help_text='Enter name of the Trail.', max_length=255, verbose_name='Name of trail section')),
                ('notes', models.TextField(help_text='Enter some notes regarding the above named trail', max_length=300, null=True, verbose_name='Notes on named Trail', blank=True)),
                ('image', models.ImageField(help_text='An image of the trail section. Most browsers support dragging the image directly on to the "Choose File" button above.', upload_to=b'images/trail_sections', null=True, verbose_name='Image file', blank=True)),
                ('geometry', django.contrib.gis.db.models.fields.LineStringField(help_text='Enter the geometry of the trail section (as line string).', srid=4326, null=True, verbose_name='Geometry', blank=True)),
                ('slug', models.SlugField()),
                ('time_start', models.DateTimeField(help_text='Enter time when the trail started on that section.', null=True, verbose_name='Start Time', blank=True)),
                ('time_end', models.DateTimeField(help_text='Enter time when the trail ended on that section.', null=True, verbose_name='End Time', blank=True)),
                ('grade_id', models.ForeignKey(to='trail.Grade')),
            ],
            options={
                'ordering': ['name'],
                'verbose_name_plural': 'Trail Sections',
            },
        ),
        migrations.AlterUniqueTogether(
            name='trailsection',
            unique_together=set([('name', 'grade_id')]),
        ),
    ]
