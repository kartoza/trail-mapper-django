from rest_framework.generics import ListAPIView

from ..models.trail import Trail
from ..serializers.trail import TrailSerializer


__author__ = 'Alison Mukoma <alison@kartoza.com>'
__date__ = '24/10/17'
__license__ = "GPL"
__copyright__ = 'kartoza.com'


class TrailListApiView(ListAPIView):
    """
    Api to list all available trails.
    """

    queryset = Trail.Category.objects.all()
    serializer_class = TrailSerializer
    lookup_field = 'slug'
