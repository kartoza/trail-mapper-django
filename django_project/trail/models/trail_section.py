# coding=utf-8
"""Model definitions for a trail app"""

import os

from django.contrib.gis.db import models
from django.utils.translation import ugettext_lazy as _
from django.utils.text import slugify
from django.conf.global_settings import MEDIA_ROOT

from unidecode import unidecode

from core.settings.contrib import STOP_WORDS
from grade import Grade


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

    existing_trail_section = TrailSection.objects.all()
    new_trail_section_name = '%s' % (_name)
    for trail_section in existing_trail_section:
        if _name == trail_section.name:
            _count_names = TrailSection.objects.filter(
                name=_name)
            count = _count_names.count() + 1
            new_trail_section_name = '%s %s' % (_name, count)
            break

    return new_trail_section_name


class TrailSection(models.Model):
    "Model definition of a Trail Section."

    name = models.CharField(
        _('Name of trail section'),
        max_length = 255,
        null=False,
        blank=False,
        help_text = _('Enter name of the Trail.')
    )

    notes = models.TextField(
        _("Notes on named Trail"),
        max_length = 300,
        null = True,
        blank = True,
        help_text = _('Enter some notes regarding the above named trail')
    )

    image = models.ImageField(
        _('Image file'),
        null=True,
        blank=True,
        upload_to=os.path.join(MEDIA_ROOT, 'images/trail_sections'),
        help_text = _(
            'An image of the trail section. '
            'Most browsers support dragging the image directly on to the '
            '"Choose File" button above.')
    )

    geometry = models.LineStringField(
        _('Geometry'),
        null=True,
        blank=True,
        help_text = _('Enter the geometry of the trail section (as line string).')
    )


    slug = models.SlugField()
    objects = models.Manager()
    grade_id = models.ForeignKey(Grade)

    time_start = models.DateTimeField(
        _("Start Time"),
        auto_now=False,
        blank=True,
        null=True,
        help_text=_('Enter time when the trail started on that section.')
    )

    time_end = models.DateTimeField(
        _("End Time"),
        auto_now=False,
        blank=True,
        null=True,
        help_text=_('Enter time when the trail ended on that section.')
    )

    class Meta:
        ordering = ['name']
        unique_together = [
            'name', 'grade_id',
        ]
        app_label = 'trail'
        verbose_name_plural = 'Trail Section'


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
        super(TrailSection, self).save(*args, **kwargs)
