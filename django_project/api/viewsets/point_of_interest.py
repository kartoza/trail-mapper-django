import os
from rest_framework import viewsets
from rest_framework.response import Response

from ..serializers import PointOfInterestSerialiser
from trail_mapper.models import PointOfInterest


class PointOfInterestViewSet(viewsets.ModelViewSet):
    queryset = PointOfInterest.objects.all()
    serializer_class = PointOfInterestSerialiser
    lookup_field = 'guid'

    def list(self, request, *args, **kwargs):
        # recreate the queryset here so we can be sure it fetches all data
        queryset = PointOfInterest.objects.all()
        items = []
        for item in queryset:
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
