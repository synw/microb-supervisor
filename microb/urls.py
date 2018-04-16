# -*- coding: utf-8 -*-
from django.conf.urls import url
from .views import InstancesView

urlpatterns = [
    url(r'^', InstancesView.as_view(), name="microb-index"),
]
