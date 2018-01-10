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
# from ..utils import GUIDModel

__author__ = 'Alison Mukoma <alison@kartoza.com>'
__date__ = '01/09/2018'
__license__ = "GPL"
__copyright__ = 'kartoza.com'


def increment_slug(_name):
    """Function to increment slug.

    If there already exists the trail name and colour,
    the slug will be incremented
    e.g. trail-#25HHfff, trail-#25HHfff etc.
    """

    existing_trails = Trail.objects.all()
    new_trail_name = '%s' % (_name)
    for trail in existing_trails:
        if _name == trail.name:
            _count_names = Trail.objects.filter(
                name=_name)
            _count = _count_names.count() + 1
            new_trail_name = '%s %s' % (_name, _count)
            break

    return new_trail_name


# class Trail(GUIDModel, models.Model):
class Trail(models.Model):
    "Model definition of a Trail."

    name = models.CharField(
        _('Name of Trail'),
        max_length = 255,
        null = False,
        blank = False,
        help_text = _('Enter name of the Trail.')
    )

    guid = models.UUIDField(
        _('GUID'),
        db_index = False,
        default=uuid_lib.uuid4,
        editable=False
    )

    notes = models.TextField(
        _("Notes on named Trail"),
        max_length = 300,
        null = True,
        blank = True,
        help_text = _('Enter some notes regarding the above named trail')
    )

    offset = models.CharField(
        _("Offset"),
        max_length=255,
        null = True,
        blank = True,
        help_text = _('Enter offset value i.e -2')
    )

    colour = models.CharField(
        _("Colour"),
        max_length = 255,
        null=True,
        blank = True,
        help_text = _('Enter colour of the trail.')
    )

    image = models.ImageField(
        _('Image file'),
        null=True,
        blank=True,
        upload_to=os.path.join(MEDIA_ROOT, 'images/trail'),
        help_text = _(
            'An image of the trail. '
            'Most browsers support dragging the image directly on to the '
            '"Choose File" button above.')
    )

    geometry = models.PointField()

    slug = models.SlugField()
    objects = models.Manager()

    class Meta:
        ordering = ['name']
        unique_together = [
            'name', 'offset',
        ]
        # app_label = 'trail'
        verbose_name_plural = "Trails"


        def _str__(self):
            return self.__unicode__()

        def __unicode__(self):
            return '%s' % (self.name)

    def save(self, *args, **kwargs):
        if not self.pk:
            name = increment_slug(self.name)
            words = name.split()
            filtered_words = [word for word in
                              words if word.lower() not in STOP_WORDS]
            # unidecode() represents special characters (unicode data) in ASCII
            new_list = unidecode(' '.join(filtered_words))
            self.slug = slugify(new_list)[:50]
        super(Trail, self).save(*args, **kwargs)
