from rest_framework.response import Response
from rest_framework.views import APIView

from ..models.grade import Grade
from ..serializers.grade import GradeSerializer


__author__ = 'Alison Mukoma <alison@kartoza.com>'
__date__ = '24/10/17'
__license__ = "GPL"
__copyright__ = 'kartoza.com'


class GradeListApiView(APIView):
    """
    Api to list all available grades on GET request.
    """

    def get(self, request):
        grades = Grade.objects.all().order_by('name')

        serializer = GradeSerializer(grades, many=True)
        return Response(serializer.data)
