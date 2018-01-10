from rest_framework.response import Response
from rest_framework.views import APIView

from ..models.trail_sections import TrailSections
from ..serializers.trail_sections import TrailSectionsSerializer


__author__ = 'Alison Mukoma <alison@kartoza.com>'
__date__ = '24/10/17'
__license__ = "GPL"
__copyright__ = 'kartoza.com'


class TrailSectionsListApiView(APIView):
    """
    Api to list all available trail sections on GET request.
    """

    def get(self, request):
        trail_sections = TrailSections.objects.all().order_by('name')

        serializer = TrailSectionsSerializer(trail_sections, many=True)
        return Response(serializer.data)
