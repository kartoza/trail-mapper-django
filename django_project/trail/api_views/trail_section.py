from rest_framework.response import Response
from rest_framework.views import APIView

from ..models.trail_section import TrailSection
from ..serializers.trail_section import TrailSectionSerializer


__author__ = 'Alison Mukoma <alison@kartoza.com>'
__date__ = '24/10/17'
__license__ = "GPL"
__copyright__ = 'kartoza.com'


class TrailSectionListApiView(APIView):
    """
    Api to list all available trail section data on GET request.
    """

    def get(self, request):
        trail_section = TrailSection.objects.all().order_by('name')

        serializer = TrailSectionSerializer(trail_section, many=True)
        return Response(serializer.data)
