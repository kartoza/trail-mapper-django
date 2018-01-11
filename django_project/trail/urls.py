from __future__ import absolute_import
# coding=utf-8
"""URI Routing configuration for this apps."""
from django.conf.urls import url

from .api_views.trail import (
    TrailListApiView,
    TrailFilterByIDAPIView,
    TrailCreateAPIView
    )
from .api_views.trail_section import (TrailSectionListApiView,
                                      TrailSectionFilterByIDAPIView)
from .api_views.trail_sections import TrailSectionsListApiView
from .api_views.category import CategoryListApiView
from .api_views.grade import GradeListApiView
from .api_views.point_of_interest import PointOfInterestListApiView

urlpatterns = [

    url(
        r'^api/list_trail/',
         TrailListApiView.as_view(),
        name='api-get-trail-list'),
    url(
        r'^api/create_trail/',
        TrailCreateAPIView.as_view(),
        name='api-trail-create'),
    url(
        r'^api/trail/(?P<trail_id>.+)/',
        TrailFilterByIDAPIView.as_view(),
        name='api-get-trail-by-id'),
    url(
        r'^api/list_trail_section/',
        TrailSectionListApiView.as_view(),
        name='api-get-trail-section'),
    url(
        r'^api/trail_section/(?P<trail_section_id>.+)/',
        TrailSectionFilterByIDAPIView.as_view(),
        name='api-get-trail-section-by-id'),
    url(
        r'^api/list_trail_sections/',
        TrailSectionsListApiView.as_view(),
        name='api-get-trail-sections'),
    url(
        r'^api/list_category/',
        CategoryListApiView.as_view(),
        name='api-get-category'),
    url(
        r'^api/list_grade/',
        GradeListApiView.as_view(),
        name='api-get-grade'),
    url(
        r'^api/list_poi/',
        PointOfInterestListApiView.as_view(),
        name='api-get-poi')
]
