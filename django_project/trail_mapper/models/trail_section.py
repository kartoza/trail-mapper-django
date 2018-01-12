# coding=utf-8
"""Model definitions for a trail_mapper app"""

import os
import uuid as uuid_lib

from django.contrib.gis.db import models
from django.utils.translation import ugettext_lazy as _
from django.conf.global_settings import MEDIA_ROOT


from grade import Grade


__author__ = 'Alison Mukoma <alison@kartoza.com>'
__date__ = '01/10/2018'
__license__ = "GPL"
__copyright__ = 'kartoza.com'


class TrailSection(models.Model):
    "Model definition of a Trail Section."

    guid = models.UUIDField(
        _('GUID'),
        db_index=False,
        null=False,
        default=uuid_lib.uuid4,
        editable=False
    )

    name = models.CharField(
        _('Name of trail_mapper section'),
        max_length = 255,
        help_text = _('Enter name of the Trail.')
    )

    notes = models.TextField(
        _("Notes on named Trail"),
        max_length = 300,
        null = True,
        blank = True,
        help_text = _('Enter some notes regarding the above named trail_mapper')
    )

    image = models.ImageField(
        _('Image file'),
        null=True,
        blank=True,
        upload_to=os.path.join(MEDIA_ROOT, 'images/trail_sections'),
        help_text = _(
            'An image of the trail_mapper section. '
            'Most browsers support dragging the image directly on to the '
            '"Choose File" button above.')
    )

    # 3 dimensions to support z
    geom = models.LineStringField(srid=4326, dim=3, geography=True)

    slug = models.SlugField(
        null=True,
        blank=True
    )
    objects = models.Manager()
    grade = models.ForeignKey(Grade)

    time_start = models.DateTimeField(
        _("Start Time"),
        auto_now=False,
        blank=True,
        null=True,
        help_text=_('Enter time when the trail_mapper started on that section.')
    )

    time_end = models.DateTimeField(
        _("End Time"),
        auto_now=False,
        blank=True,
        null=True,
        help_text=_('Enter time when the trail_mapper ended on that section.')
    )

    class Meta:
        app_label = 'trail_mapper'
        verbose_name_plural = 'Trail Section'


    def _str__(self):
        return self.__unicode__()

    def __unicode__(self):
        return '%s' % (self.name)
