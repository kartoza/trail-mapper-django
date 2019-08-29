# coding=utf-8
"""URI Routing configuration for this apps."""
from django.conf.urls import include, url
from rest_framework import routers

from viewsets import (
    CategoryViewSet,
    GradeViewSet,
    PointOfInterestViewSet,
    PointOfInterestGeoJSONViewSet,
    TrailViewSet,
    TrailSectionViewSet,
    TrailSectionGeoJSONViewSet,
    TrailSectionsViewSet)

# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'category', CategoryViewSet)
router.register(r'grade', GradeViewSet)
router.register(r'point_of_interest', PointOfInterestViewSet)
router.register(r'trail', TrailViewSet)
router.register(r'trail_section', TrailSectionViewSet)
router.register(r'trail_sections', TrailSectionsViewSet)
router.register(r'trail_section_GeoJSON', TrailSectionGeoJSONViewSet)
router.register(r'point_of_interest_GeoJSON', PointOfInterestGeoJSONViewSet)
urlpatterns = [
    url(r'^', include(router.urls), name='api'),
    url(r'^api-auth/',
        include('rest_framework.urls', namespace='rest_framework'))
]

