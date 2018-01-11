from rest_framework.generics import ListAPIView

from ..models.trail_sections import TrailSections
from ..serializers.trail_sections import TrailSectionsSerializer


__author__ = 'Alison Mukoma <alison@kartoza.com>'
__date__ = '24/10/17'
__license__ = "GPL"
__copyright__ = 'kartoza.com'


class TrailSectionsListApiView(ListAPIView):
    """
       Api to list all available trail sections on GET request.
    """

    queryset = TrailSections.Category.objects.all()
    serializer_class = TrailSectionsSerializer
    lookup_field = 'slug'
