from rest_framework import serializers
from trail_mapper.models.trail_section import TrailSection

__author__ = 'Alison Mukoma <alison@kartoza.com>'
__date__ = '01/10/2018'
__license__ = "GPL"
__copyright__ = 'kartoza.com'


class TrailSectionSerializer(serializers.ModelSerializer):
    """Serializer class for a trail_mapper section model."""

    class Meta:
        model = TrailSection
        url_field_name = 'guid'
        fields = [
            'guid',
            'name',
            'grade',
            'image',
            'notes',
            'geom'
        ]

