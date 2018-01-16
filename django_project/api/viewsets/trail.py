import os
from rest_framework import viewsets
from rest_framework.response import Response

from ..serializers import TrailSerializer
from trail_mapper.models import Trail


class TrailViewSet(viewsets.ModelViewSet):
    # recreate the queryset her so we can be sure it fetches all data
    queryset = Trail.objects.all()
    serializer_class = TrailSerializer
    lookup_field = 'guid'

    def list(self, request, *args, **kwargs):
        # recreate the queryset her so we can be sure it fetches all data
        trail_queryset = Trail.objects.all()
        items = []
        for item in trail_queryset:
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
