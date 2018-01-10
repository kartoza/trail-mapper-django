# coding=utf-8
"""Model definitions for a trail app"""

import os

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


def increment_slug(_name):
    """Function to increment slug.

    If there already exists the trail name and colour,
    the slug will be incremented
    e.g. trail-#25HHfff, trail-#25HHfff etc.
    """

    existing_grades = Grade.objects.all()
    new_grade_name = '%s' % (_name)
    for grade in existing_grades:
        if _name == grade.name:
            _count_names = Grade.objects.filter(
                name=_name)
            count = _count_names.count() + 1
            new_grade_name = '%s %s' % (_name, count)
            break

    return new_grade_name


class Grade(models.Model):
    "Model definition of a Trail."

    name = models.CharField(
        _('Grade Name'),
        max_length = 255,
        null=False,
        blank=False,
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

    slug = models.SlugField()
    objects = models.Manager()

    class Meta:
        ordering = ['name']
        app_label = 'trail'
        verbose_name_plural = "Grades"


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
        super(Grade, self).save(*args, **kwargs)
