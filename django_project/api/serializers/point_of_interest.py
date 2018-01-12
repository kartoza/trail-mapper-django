from rest_framework import serializers
from trail_mapper.models.point_of_interest import PointOfInterest

__author__ = 'Alison Mukoma <alison@kartoza.com>'
__date__ = '01/10/2018'
__license__ = "GPL"
__copyright__ = 'kartoza.com'


class POISerializer(serializers.ModelSerializer):
    """Serializer class for a Point of Interest model."""

    class Meta:
        model = PointOfInterest
        url_field_name = 'image'
        fields = [
            'guid',
            'name',
            'image',
            'notes',
            'geom',
            'trail_section',
            'category'
        ]

