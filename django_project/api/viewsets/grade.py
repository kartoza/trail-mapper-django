from rest_framework import viewsets
from rest_framework.response import Response

from ..serializers import GradeSerializer
from trail_mapper.models import Grade


class GradeViewSet(viewsets.ModelViewSet):
    queryset = Grade.objects.all()
    serializer_class = GradeSerializer
    lookup_field = 'slug'
