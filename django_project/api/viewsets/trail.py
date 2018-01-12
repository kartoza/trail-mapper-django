import os
from rest_framework import viewsets
from rest_framework.response import Response

from ..serializers import TrailSerializer
from trail_mapper.models import Trail


class TrailViewSet(viewsets.ModelViewSet):
    queryset = Trail.objects.all()
    serializer_class = TrailSerializer
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
                'notes': item.notes,
                'geom': item.geom.ewkt,
            }
            items.append(object_dict)

        content = {
            "trails": items
        }

        return Response(content)
