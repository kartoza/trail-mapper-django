import os
from rest_framework import viewsets
from rest_framework.response import Response

from ..serializers import PointOfInterestSerialiser
from trail_mapper.models import PointOfInterest


class PointOfInterestViewSet(viewsets.ModelViewSet):
    queryset = PointOfInterest.objects.all()
    serializer_class = PointOfInterestSerialiser
    lookup_field = 'slug'

    def list(self, request, *args, **kwargs):
        items = []
        for item in self.queryset:
            if item.image:
                image = item.image
                if not os.path.exists(image.path):
                    image = ''
            else:
                image = ''
            object_dict = {
                'guid': item.guid,
                'name': item.name,
                'image': image,
                'category': item.category.guid,
                'notes': item.notes,
                'geom': item.geom.ewkt,
                'trails_section': item.trail_section.guid
            }
            items.append(object_dict)

        content = {
            "points_of_interest": items
        }

        return Response(content)
