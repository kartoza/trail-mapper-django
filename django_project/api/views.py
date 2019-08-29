from rest_framework import viewsets

from serializers import (
    CategorySerializer,
    GradeSerializer,
    POISerializer,
    TrailSerializer,
    TrailSectionSerializer,
    TrailSectionsSerializer)
from trail_mapper.models import (
    Category,
    Grade,
    POI,
    Trail,
    TrailSection,
    TrailSections
)


# ViewSets define the view behavior.
class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    lookup_field = 'slug'


class GradeViewSet(viewsets.ModelViewSet):
    queryset = Grade.objects.all()
    serializer_class = GradeSerializer
    lookup_field = 'slug'


class PointOfInterestViewSet(viewsets.ModelViewSet):
    queryset = POI.objects.all()
    serializer_class = POISerializer
    lookup_field = 'slug'


class TrailViewSet(viewsets.ModelViewSet):
    queryset = Trail.objects.all()
    serializer_class = TrailSerializer
    lookup_field = 'slug'


class TrailSectionViewSet(viewsets.ModelViewSet):
    queryset = TrailSection.objects.all()
    serializer_class = TrailSectionSerializer
    lookup_field = 'slug'


class TrailSectionsViewSet(viewsets.ModelViewSet):
    """This is the m2m join of trails and trail_sections."""
    queryset = TrailSections.objects.all()
    serializer_class = TrailSectionsSerializer
    lookup_field = 'slug'
