from rest_framework import viewsets
from rest_framework.response import Response

from ..serializers import TrailSectionSerializer
from trail_mapper.models import TrailSection


class TrailSectionViewSet(viewsets.ModelViewSet):
    queryset = TrailSection.objects.all()
    serializer_class = TrailSectionSerializer
    lookup_field = 'slug'

