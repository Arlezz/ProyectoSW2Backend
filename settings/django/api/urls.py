# -*- coding: utf-8 -*-

from django.conf.urls import url, include
from django.views.generic import RedirectView
from rest_framework.authtoken.views import obtain_auth_token

from .views import region, subcategory, category, size, public

urlpatterns = [
    url(r'^$', RedirectView.as_view(url='/dashboard/')),
    url('region/', region, name='region'),
    url('subcategory/', subcategory, name='subcategory'),
    url('category/', category, name='category'),
    url('size/', size, name='size'),
    url('public/', public, name='public'),
    url('api-token-auth/', obtain_auth_token, name='api_token_auth'),
]
