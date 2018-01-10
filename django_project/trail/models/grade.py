# coding=utf-8
"""Model definitions for a trail app"""

import os
import uuid as uuid_lib

from django.contrib.gis.db import models
from django.utils.translation import ugettext_lazy as _
from django.utils.text import slugify
from django.conf.global_settings import MEDIA_ROOT

from unidecode import unidecode

from core.settings.contrib import STOP_WORDS


__author__ = 'Alison Mukoma <alison@kartoza.com>'
__date__ = '01/10/2018'
__license__ = "GPL"
__copyright__ = 'kartoza.com'


class Grade(models.Model):
    "Model definition of a Trail."

    guid = models.UUIDField(
        _('GUID'),
        primary_key=False,
        default=uuid_lib.uuid4,
        editable=False)

    name = models.CharField(
        _('Grade Name'),
        max_length = 255,
        help_text = _('Enter Grade name of the Trail.')
    )

    image = models.ImageField(
        _('Image file'),
        null=True,
        blank=True,
        upload_to=os.path.join(MEDIA_ROOT, 'images/trail_grade'),
        help_text = _(
            'An image of the trail grade. '
            'Most browsers support dragging the image directly on to the '
            '"Choose File" button above.')
    )

    slug = models.SlugField(
        null=True,
        blank=True
    )

    objects = models.Manager()

    class Meta:
        ordering = ['name']
        app_label = 'trail'
        verbose_name_plural = "Grades"


        def _str__(self):
            return self.__unicode__()

        def __unicode__(self):
            return '%s' % (self.name)
