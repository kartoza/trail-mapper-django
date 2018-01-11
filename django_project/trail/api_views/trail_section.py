from django.db.models import Q

from rest_framework.filters import SearchFilter

from rest_framework.generics import (
    ListAPIView,
    CreateAPIView,
    UpdateAPIView
    )

from ..models.trail_section import TrailSection
from ..serializers.trail_section import TrailSectionSerializer


__author__ = 'Alison Mukoma <alison@kartoza.com>'
__date__ = '24/10/17'
__license__ = "GPL"
__copyright__ = 'kartoza.com'


class TrailSectionListApiView(ListAPIView):
    """Api to list all available trail section data on GET request.
    """

    queryset = TrailSection.objects.all()
    serializer_class = TrailSectionSerializer


class TrailSectionFilterByIDAPIView(ListAPIView):
    """API to return a single trail section
       with the trail section ID parsed in the url.
    """
    serializer_class = TrailSectionSerializer
    filter_backends = [SearchFilter]
    search_fields = ['id', 'name']

    def get_queryset(self, *args, **kwargs):
        """Returns trails if a parsed id matches trail section record
           in the database by filtering against an `id` query parameter in the URL.
        """

        queryset_list = TrailSection.objects.all()
        query = self.request.Get.get('q')
        if query:
            queryset_list = queryset_list.get(
                Q(name__icontains=query)
            ).distinct()
        return queryset_list


class TrailSectionCreateAPIView(CreateAPIView):
    """API to allow client create a new trail section on
    the server.
    """
    queryset = TrailSection.objects.all()
    serializer_class = TrailSectionSerializer



class TrailSectionUpdateAPIView(UpdateAPIView):
    """API to allow client update an existing Trail section
     entry on the server.
    """
    queryset = TrailSection.objects.all()
    serializer_class = TrailSectionSerializer
    lookup_field = 'slug'
