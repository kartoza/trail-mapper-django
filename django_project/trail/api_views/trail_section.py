from rest_framework.generics import ListAPIView

from ..models.trail_section import TrailSection
from ..serializers.trail_section import TrailSectionSerializer


__author__ = 'Alison Mukoma <alison@kartoza.com>'
__date__ = '24/10/17'
__license__ = "GPL"
__copyright__ = 'kartoza.com'


class TrailSectionListApiView(ListAPIView):

    """Api to list all available trail section data on GET request.


    queryset = TrailSection.objects.all()
    serializer_class = TrailSectionSerializer


class TrailSectionFilterByIDAPIView(ListAPIView):
    """API to return a single trail section
       with the trail section ID parsed in the url.
    """
    serializer_class = TrailSectionSerializer

    def get_queryset(self):
        """Returns trails if a parsed id matches trail section record
            in the database by filtering against an `id` query parameter in the URL.
        """

        queryset = TrailSection.objects.all()
        trail_section_id = self.request.query_params.get('trail_section_id', None)

        if trail_section_id is not None:
            queryset = queryset.objects.filter(id=trail_section_id)
        return queryset

