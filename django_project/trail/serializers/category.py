from rest_framework import serializers
from ..models.category import Category

__author__ = 'Alison Mukoma <alison@kartoza.com>'
__date__ = '01/10/2018'
__license__ = "GPL"
__copyright__ = 'kartoza.com'


class CategorySerializer(serializers.ModelSerializer):
    """Serializer class for The Category model."""

    class Meta:
        model = Category
        fields = ('order', 'image')
