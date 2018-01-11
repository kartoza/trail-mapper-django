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

    queryset = Trail.objects.all()
    serializer_class = TrailSerializer
    lookup_field = 'slug'


class TrailFilterByIDAPIView(ListAPIView):
    """API to return a single trail
       with the trail ID parsed in the url.
    """
    serializer_class = TrailSerializer

    def get_queryset(self):
        """
            Returns trails if a parsed id matches trail record in the database,
            by filtering against an `id` query parameter in the URL.
        """

        queryset = Trail.objects.all()
        trail_id = self.request.query_params.get('trail_id', None)

        if trail_id is not None:
            queryset = queryset.objects.filter(id=trail_id)
        return queryset
