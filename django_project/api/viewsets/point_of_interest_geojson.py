
from rest_framework import viewsets

from ..serializers import PointOfInterestGeoJSONSerialiser
from trail_mapper.models import PointOfInterest


class PointOfInterestGeoJSONViewSet(viewsets.ModelViewSet):
    queryset = PointOfInterest.objects.all()
    serializer_class = PointOfInterestGeoJSONSerialiser
    lookup_field = 'guid'



