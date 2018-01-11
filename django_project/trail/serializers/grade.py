from rest_framework import serializers
from ..models.grade import Grade

__author__ = 'Alison Mukoma <alison@kartoza.com>'
__date__ = '01/10/2018'
__license__ = "GPL"
__copyright__ = 'kartoza.com'


class GradeSerializer(serializers.ModelSerializer):
    """Serializer class for the Grade model."""

    class Meta:
        model = Grade
        url_field_name = 'image'
        fields = [
            'guid',
            'name',
            'image'
        ]
