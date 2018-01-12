from rest_framework import viewsets
from rest_framework.response import Response

from ..serializers import TrailSerializer
from trail_mapper.models import Trail


class TrailViewSet(viewsets.ModelViewSet):
    queryset = Trail.objects.all()
    serializer_class = TrailSerializer
    lookup_field = 'slug'
