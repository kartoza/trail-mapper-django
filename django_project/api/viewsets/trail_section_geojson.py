from rest_framework import viewsets

from ..serializers import TrailSectionGeoJSONSerializer
from trail_mapper.models import TrailSection


class TrailSectionGeoJSONViewSet(viewsets.ModelViewSet):
    queryset = TrailSection.objects.all()
    serializer_class = TrailSectionGeoJSONSerializer
    lookup_field = 'guid'

