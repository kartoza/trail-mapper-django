from rest_framework.generics import ListAPIView

from ..models.point_of_interest import POI
from ..serializers.point_of_interest import POISerializer


__author__ = 'Alison Mukoma <alison@kartoza.com>'
__date__ = '24/10/17'
__license__ = "GPL"
__copyright__ = 'kartoza.com'


class PointOfInterestListApiView(ListAPIView):
    """
       Api to list all available point of interest on GET request.
    """

    queryset = POI.Category.objects.all()
    serializer_class = POISerializer
    lookup_field = 'slug'
