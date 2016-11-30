# -*- coding: utf-8 -*-
from django.conf.urls.defaults import url

from .views import LoupeImageDetailView

urlpatterns = [
    url(r'^(?P<slug>[-_\w]+)/$', LoupeImageDetailView.as_view(),
        name='loupeimage-detail'),
    ]
