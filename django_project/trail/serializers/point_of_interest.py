from rest_framework import serializers
from ..models.point_of_interest import POI

__author__ = 'Alison Mukoma <alison@kartoza.com>'
__date__ = '01/10/2018'
__license__ = "GPL"
__copyright__ = 'kartoza.com'


class POISerializer(serializers.ModelSerializer):
    """Serializer class for a Point of Interest model."""

    class Meta:
        model = POI
        fields = ('name', 'notes', 'guid')
