from rest_framework.response import Response
from rest_framework.views import APIView

from ..models.point_of_interest import POI
from ..serializers.point_of_interest import POISerializer


__author__ = 'Alison Mukoma <alison@kartoza.com>'
__date__ = '24/10/17'
__license__ = "GPL"
__copyright__ = 'kartoza.com'


class PointOfInterestListApiView(APIView):
    """
    Api to list all available point of interest on GET request.
    """

    def get(self, request):
        pois = POI.objects.all().order_by('name')

        serializer = POISerializer(pois, many=True)
        return Response(serializer.data)
