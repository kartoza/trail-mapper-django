import os
from rest_framework import viewsets
from rest_framework.response import Response

from ..serializers import CategorySerializer
from trail_mapper.models import Category


# ViewSets define the view behavior.
class CategoryViewSet(viewsets.ModelViewSet):
    """API Viewset for Categories."""

    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    lookup_field = 'guid'

    def list(self, request, *args, **kwargs):
        # Recreate the queryset here so it fetches all data
        queryset = Category.objects.all()
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
            "categories": items
        }

        return Response(content)
