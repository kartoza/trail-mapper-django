# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.contrib.gis.db.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('trail', '0004_auto_20180110_0904'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(help_text='Enter Category name.', max_length=255, verbose_name='Name of Category')),
                ('image', models.ImageField(help_text='An image of the trail section. Most browsers support dragging the image directly on to the "Choose File" button above.', upload_to=b'images/trail_category', null=True, verbose_name='Image file', blank=True)),
                ('geometry', django.contrib.gis.db.models.fields.LineStringField(help_text='Enter the geometry of the tcategory (as line string).', srid=4326, null=True, verbose_name='Geometry', blank=True)),
                ('slug', models.SlugField()),
            ],
            options={
                'ordering': ['name'],
                'verbose_name_plural': 'Trail Categories',
            },
        ),
        migrations.CreateModel(
            name='POI',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(help_text='Enter name of the Point of Interest.', max_length=255, null=True, verbose_name='Name of Point of Interest(POI)', blank=True)),
                ('notes', models.TextField(help_text='Enter some notes regarding the above named POI', max_length=300, null=True, verbose_name='Notes on named POI', blank=True)),
                ('image', models.ImageField(help_text='An image of the trail section. Most browsers support dragging the image directly on to the "Choose File" button above.', upload_to=b'images/poi', null=True, verbose_name='Image file', blank=True)),
                ('slug', models.SlugField()),
                ('category', models.ForeignKey(to='trail.Category')),
                ('trail_section', models.ForeignKey(to='trail.TrailSection', blank=True)),
            ],
            options={
                'ordering': ['name'],
                'verbose_name_plural': 'Point of Interest (POI)',
            },
        ),
    ]
