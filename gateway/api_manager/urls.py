from django.conf.urls import url

import os

from gateway.api_manager import views

urlpatterns = [
	url(r'^superm$', views.superm)
]
