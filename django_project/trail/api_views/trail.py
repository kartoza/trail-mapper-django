from django.db.models import Q

from rest_framework.filters import (
    SearchFilter,
    OrderingFilter
)
from rest_framework.generics import (
    ListAPIView,
    CreateAPIView
    )
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
    filter_backends = [SearchFilter]
    search_fields = ['id', 'name']

    def get_queryset(self, *args, **kwargs):

        """
            Returns trails if a parsed id matches trail record in the database,
            by filtering against an `id` query parameter in the URL.
        """

        queryset_list = Trail.objects.all()
        query = self.request.Get.get('q')
        if query:
            queryset_list = queryset_list.get(
                Q(name__icontains=query)
            ).distinct()
        return queryset_list



class TrailCreateAPIView(CreateAPIView):
    """API to allow client create a new Trail on
    the server.
    """
    queryset = Trail.objects.all()
    serializer_class = TrailSerializer
    
