from rest_framework.response import Response
from rest_framework.views import APIView

from ..models.trail import Trail
from ..serializers.trail import TrailSerializer


__author__ = 'Alison Mukoma <alison@kartoza.com>'
__date__ = '24/10/17'
__license__ = "GPL"
__copyright__ = 'kartoza.com'


class TrailListApiView(APIView):
    """
    Api to list all available trails.
    """

    def get(self, request):
        trails = Trail.objects.all().order_by('name')

        serializer = TrailSerializer(trails, many=True)
        return Response(serializer.data)
