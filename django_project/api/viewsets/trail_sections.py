from rest_framework import viewsets
from rest_framework.response import Response

from ..serializers import TrailSectionsSerializer
from trail_mapper.models import TrailSections



class TrailSectionsViewSet(viewsets.ModelViewSet):
    """This is the m2m join of trails and trail_sections."""
    queryset = TrailSections.objects.all()
    serializer_class = TrailSectionsSerializer
    lookup_field = 'slug'
