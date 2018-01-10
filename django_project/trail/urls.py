# coding=utf-8
"""URI Routing configuration for this apps."""
from django.conf.urls import url

from trail.api_views.trail import TrailListView


urlpatterns = [
     url(
        r'^api/list_trail/',
        TrailListView.as_view(),
        name='api-get-trail-list')
     ]
