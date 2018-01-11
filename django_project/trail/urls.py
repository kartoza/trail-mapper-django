from __future__ import absolute_import
# coding=utf-8
"""URI Routing configuration for this apps."""
from django.conf.urls import url

from .api_views.trail import (
    TrailListApiView,
<<<<<<< HEAD
<<<<<<< HEAD
=======
    TrailFilterByIDAPIView,
>>>>>>> aebd203bc14829953aa9011fad3142a802784d56
    TrailCreateAPIView
    )
from .api_views.trail_section import (TrailSectionListApiView,
                                      TrailSectionFilterByIDAPIView)
<<<<<<< HEAD
=======

>>>>>>> aebd203bc14829953aa9011fad3142a802784d56
=======
    TrailCreateAPIView
    )
from .api_views.trail_section import (
    TrailSectionListApiView,
    TrailSectionCreateAPIView
)
>>>>>>> f93601528ddb64db47999f6c5ac14f69858298ef
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
<<<<<<< HEAD

        r'^api/trail/(?P<trail_id>.+)/',
        TrailFilterByIDAPIView.as_view(),
        name='api-get-trail-by-id'),
    url(
=======
>>>>>>> f93601528ddb64db47999f6c5ac14f69858298ef
        r'^api/list_trail_section/',
        TrailSectionListApiView.as_view(),
        name='api-get-trail-section'),
    url(
<<<<<<< HEAD
<<<<<<< HEAD
        r'^api/create_trail_section/',
        TrailSectionCreateAPIView.as_view(),
        name='api-trail-section-create'),
=======
        r'^api/trail_section/(?P<trail_section_id>.+)/',
        TrailSectionFilterByIDAPIView.as_view(),
        name='api-get-trail-section-by-id'),
>>>>>>> aebd203bc14829953aa9011fad3142a802784d56
=======
        r'^api/create_trail_section/',
        TrailSectionCreateAPIView.as_view(),
        name='api-trail-section-create'),

>>>>>>> f93601528ddb64db47999f6c5ac14f69858298ef
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

