from rest_framework.response import Response
from rest_framework.views import APIView

from ..models.category import Category
from ..serializers.category import CategorySerializer


__author__ = 'Alison Mukoma <alison@kartoza.com>'
__date__ = '24/10/17'
__license__ = "GPL"
__copyright__ = 'kartoza.com'


class CategoryListApiView(APIView):
    """
    Api to list all available categories on GET request.
    """

    def get(self, request):
        categories = Category.objects.all().order_by('order')

        serializer = CategorySerializer(categories, many=True)
        return Response(serializer.data)
