# coding=utf-8
"""URI Routing configuration for this apps."""
from django.conf.urls import url

from ..trail.api_views.trail import TrailListApiView
from ..trail.api_views.trail_section import TrailSectionListApiView
from ..trail.api_views.trail_sections import TrailSectionsListApiView
from ..trail.api_views.category import CategoryListApiView
from ..trail.api_views.grade import GradeListApiView
from ..trail.api_views.point_of_interest import PointOfInterestListApiView


urlpatterns = [

     url(
        r'^api/list_trail/',
         TrailListApiView.as_view(),
        name='api-get-trail-list'),
    url(
        r'^api/list_trail_section/',
        TrailSectionListApiView.as_view(),
        name='api-get-trail-section'),
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
