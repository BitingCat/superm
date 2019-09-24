from django.conf.urls import url, include

import os

urlpatterns = [
	url(r'^', include('gateway.api_manager.urls'))
]
