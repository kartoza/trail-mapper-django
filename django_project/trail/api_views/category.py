from rest_framework.generics import ListAPIView

from ..models.category import Category
from ..serializers.category import CategorySerializer


__author__ = 'Alison Mukoma <alison@kartoza.com>'
__date__ = '24/10/17'
__license__ = "GPL"
__copyright__ = 'kartoza.com'


class CategoryListApiView(ListAPIView):
    """
    Api to list all available Categories
    on GET request.
    """

    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    lookup_field = 'slug'
