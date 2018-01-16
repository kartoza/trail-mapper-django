import os
from rest_framework import viewsets
from rest_framework.response import Response

from ..serializers import GradeSerializer
from trail_mapper.models import Grade


class GradeViewSet(viewsets.ModelViewSet):
    queryset = Grade.objects.all()
    serializer_class = GradeSerializer
    lookup_field = 'slug'

    def list(self, request, *args, **kwargs):
        # recreate the queryset here so it gets all data
        queryset = Grade.objects.all()
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
                'image': image
            }
            items.append(object_dict)

        content = {
            "grades": items
        }

        return Response(content)
