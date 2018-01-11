from rest_framework import serializers
from ..models.trail import Trail

__author__ = 'Alison Mukoma <alison@kartoza.com>'
__date__ = '01/10/2018'
__license__ = "GPL"
__copyright__ = 'kartoza.com'


class TrailSerializer(serializers.ModelSerializer):
    """Serializer class for Trail model."""

    class Meta:
        model = Trail
        fields = ('guid', 'name', 'image', 'notes',
                  'colour', 'id', 'geometry', 'offset')
        url_field_name = 'image'