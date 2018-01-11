from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import (
    DestroyAPIView,
    ListAPIView,
    UpdateAPIView,
    RetrieveAPIView
    )

from ..models.grade import Grade
from ..serializers.grade import GradeSerializer


__author__ = 'Alison Mukoma <alison@kartoza.com>'
__date__ = '24/10/17'
__license__ = "GPL"
__copyright__ = 'kartoza.com'


class GradeListApiView(ListAPIView):
    """
    Api to list all available grades on GET request.
    """

    queryset = Grade.objects.all()
    serializer_class = GradeSerializer
    lookup_field = 'slug'

class GradeUpdateAPIView(UpdateAPIView):
    queryset = Grade.objects.all()
    serializer_class = GradeSerializer
    lookup_field = 'slug'