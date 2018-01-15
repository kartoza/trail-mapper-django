# coding=utf-8
"""URI Routing configuration for this apps."""
from django.conf.urls import include, url
from rest_framework import routers

from viewsets import (
    CategoryViewSet,
    GradeViewSet,
    PointOfInterestViewSet,
    TrailViewSet,
    TrailSectionViewSet,
    TrailSectionsViewSet)

# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'category', CategoryViewSet)
router.register(r'grade', GradeViewSet)
router.register(r'pointofinterest', PointOfInterestViewSet)
router.register(r'trail', TrailViewSet)
router.register(r'trail_section', TrailSectionViewSet)
router.register(r'trail_sections', TrailSectionsViewSet)

urlpatterns = [
    url(r'^', include(router.urls), name='api'),
    url(r'^api-auth/',
        include('rest_framework.urls', namespace='rest_framework'))
]

