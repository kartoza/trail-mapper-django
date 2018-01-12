# coding=utf-8
"""Model definitions for a trail_mapper app"""
import os
import uuid as uuid_lib

from django.contrib.gis.db import models
from django.utils.translation import ugettext_lazy as _
from django.conf.global_settings import MEDIA_ROOT

from category import Category
from trail_section import TrailSection


__author__ = 'Alison Mukoma <alison@kartoza.com>'
__date__ = '01/10/2018'
__license__ = "GPL"
__copyright__ = 'kartoza.com'


class POI(models.Model):
    "Model definition for a Point of Interest (POI)."

    guid = models.UUIDField(
        _('GUID'),
        db_index = False,
        null=False,
        default = uuid_lib.uuid4,
        editable = False
    )

    name = models.CharField(
        _('Name of Point of Interest(POI)'),
        max_length = 255,
        help_text = _('Enter name of the Point of Interest.')
    )

    notes = models.TextField(
        _("Notes on named POI"),
        max_length = 300,
        null = True,
        blank = True,
        help_text = _('Enter some notes regarding the above named POI')
    )

    image = models.ImageField(
        _('Image file'),
        null=True,
        blank=True,
        upload_to=os.path.join(MEDIA_ROOT, 'images/poi'),
        help_text = _(
            'An image of the trail_mapper section. '
            'Most browsers support dragging the image directly on to the '
            '"Choose File" button above.')
    )

    slug = models.SlugField(
        null=True,
        blank=True
    )

    geom = models.PointField(
        geography=True,
        blank=True,
        null=True,
        srid=4326
    )

    objects = models.Manager()
    category = models.ForeignKey(Category)
    trail_section = models.ForeignKey(TrailSection)

    class Meta:
        ordering = ['name']
        app_label = 'trail_mapper'
        verbose_name_plural = 'Points of Interest (POIs)'


    def _str__(self):
        return self.__unicode__()

    def __unicode__(self):
        return '%s' % (self.name)
