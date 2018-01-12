# coding=utf-8
"""URI Routing configuration for this apps."""
from django.conf.urls import url
from views import index

urlpatterns = [
    url(r'^$', index, name='trails-home'),
]

