# coding=utf-8
"""Model definitions for a trail app"""

import os

from django.contrib.gis.db import models
from django.utils.translation import ugettext_lazy as _
from django.utils.text import slugify
from django.conf.global_settings import MEDIA_ROOT

from unidecode import unidecode

from core.settings.contrib import STOP_WORDS
from category import Category
from trail_section import TrailSection


__author__ = 'Alison Mukoma <alison@kartoza.com>'
__date__ = '01/10/2018'
__license__ = "GPL"
__copyright__ = 'kartoza.com'


def increment_slug(_name):
    """Function to increment slug.

    If there already exists the trail name and colour,
    the slug will be incremented
    e.g. trail-#25HHfff, trail-#25HHfff etc.
    """

    existing_pois = POI.objects.all()
    new_poi_name = '%s' % (_name)
    for poi in existing_pois:
        if _name == poi.name:
            _count_names = POI.objects.filter(
                name=_name)
            count = _count_names.count() + 1
            new_poi_name = '%s %s' % (_name, count)
            break

    return new_poi_name


class POI(models.Model):
    "Model definition for a Point of Interest (POI)."

    name = models.CharField(
        _('Name of Point of Interest(POI)'),
        max_length = 255,
        null = True,
        blank = True,
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
            'An image of the trail section. '
            'Most browsers support dragging the image directly on to the '
            '"Choose File" button above.')
    )

    slug = models.SlugField()
    objects = models.Manager()
    category = models.ForeignKey(Category)
    trail_section = models.ForeignKey(TrailSection, blank=True)

    class Meta:
        ordering = ['name']
        app_label = 'trail'
        verbose_name_plural = 'Point of Interest (POI)'


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
        super(POI, self).save(*args, **kwargs)
