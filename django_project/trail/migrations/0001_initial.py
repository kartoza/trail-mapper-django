# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.contrib.gis.db.models.fields


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Trail',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(help_text='Enter name of the Trail.', max_length=255, verbose_name='Name of Trail')),
                ('notes', models.TextField(help_text='Enter some notes regarding the above named trail', max_length=300, null=True, verbose_name='Notes on named Trail', blank=True)),
                ('offset', models.FloatField(default=0.0, help_text='Enter offset value i.e -2', null=True, verbose_name='Offset', blank=True)),
                ('colour', models.CharField(help_text='Enter colour of the trail.', max_length=255, null=True, verbose_name='Colour', blank=True)),
                ('image', models.ImageField(help_text='An image of the trail. Most browsers support dragging the image directly on to the "Choose File" button above.', upload_to=b'images/trail', null=True, verbose_name='Image file', blank=True)),
                ('geometry', django.contrib.gis.db.models.fields.PointField(srid=4326)),
                ('slug', models.SlugField()),
            ],
            options={
                'ordering': ['name'],
                'verbose_name_plural': 'Trails',
            },
        ),
        migrations.AlterUniqueTogether(
            name='trail',
            unique_together=set([('name', 'offset')]),
        ),
    ]
