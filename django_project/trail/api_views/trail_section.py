from rest_framework.generics import ListAPIView

from ..models.trail_section import TrailSection
from ..serializers.trail_section import TrailSectionSerializer


__author__ = 'Alison Mukoma <alison@kartoza.com>'
__date__ = '24/10/17'
__license__ = "GPL"
__copyright__ = 'kartoza.com'


class TrailSectionListApiView(ListAPIView):
    """
      Api to list all available trail section data on GET request.
    """

    queryset = TrailSection.objects.all()
    serializer_class = TrailSectionSerializer
    lookup_field = 'slug'
