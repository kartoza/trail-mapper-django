# coding=utf-8
"""Model definitions for a trail_mapper app"""

from django.contrib.gis.db import models
from django.utils.translation import ugettext_lazy as _

from trail import Trail
from trail_section import TrailSection


__author__ = 'Alison Mukoma <alison@kartoza.com>'
__date__ = '01/10/2018'
__license__ = "GPL"
__copyright__ = 'kartoza.com'


class TrailSections(models.Model):
    "Model definition of a Trail Sections."

    order = models.CharField(
        _('Order'),
        max_length = 255,
        null = False,
        blank = False,
        help_text = _('Enter ordering of trail_mapper sections.')
    )

    slug = models.SlugField(
        null=True,
        blank=True
    )

    objects = models.Manager()
    trail = models.ForeignKey(Trail)
    trail_section = models.ForeignKey(TrailSection)

    class Meta:
        ordering = ['order']
        app_label = 'trail_mapper'
        verbose_name_plural = 'Trail Sections'

    def _str__(self):
        return self.__unicode__()

    def __unicode__(self):
        return '%s' % (self.order)
