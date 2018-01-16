from rest_framework_gis.serializers import GeoFeatureModelSerializer
from trail_mapper.models.point_of_interest import PointOfInterest

__author__ = 'Tim Sutton <tim@kartoza.com>'
__date__ = '01/10/2018'
__license__ = "GPL"
__copyright__ = 'kartoza.com'


class PointOfInterestGeoJSONSerialiser(GeoFeatureModelSerializer):
    """Serializer class for a Point of Interest model - GeoJSON version."""

    class Meta:
        model = PointOfInterest
        url_field_name = 'guid'
        fields = [
            'guid',
            'name',
            'image',
            'notes',
            'geom',
            'trail_section',
            'category'
        ]
        geo_field = 'geom'

