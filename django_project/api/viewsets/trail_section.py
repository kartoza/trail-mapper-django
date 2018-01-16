import os
from rest_framework import viewsets
from rest_framework.response import Response

from ..serializers import TrailSectionSerializer
from trail_mapper.models import TrailSection


class TrailSectionViewSet(viewsets.ModelViewSet):
    queryset = TrailSection.objects.all()
    serializer_class = TrailSectionSerializer
    lookup_field = 'guid'

    def list(self, request, *args, **kwargs):
        # recreate the queryset here so we can be sure it fetches all data
        section_queryset = TrailSection.objects.all()
        items = []
        for item in section_queryset.queryset:
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
                'notes': item.notes,
                'geom': item.geom.ewkt,
                'grade': item.grade.guid
            }
            items.append(object_dict)

        content = {
            "trails_sections": items
        }
        return Response(content)
