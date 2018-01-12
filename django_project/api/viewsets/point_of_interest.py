from rest_framework import viewsets
from rest_framework.response import Response

from ..serializers import POISerializer
from trail_mapper.models import PointOfInterest


class PointOfInterestViewSet(viewsets.ModelViewSet):
    queryset = PointOfInterest.objects.all()
    serializer_class = POISerializer
    lookup_field = 'slug'

