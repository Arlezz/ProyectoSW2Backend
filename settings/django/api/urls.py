# -*- coding: utf-8 -*-

from django.conf.urls import url, include
from django.views.generic import RedirectView
from rest_framework_simplejwt.views import TokenRefreshView

from .views import region, subcategory, category, size, public, MyObtainTokenPairView, register_normal_user, RegisterProviderUserSerializer

urlpatterns = [
    url(r'^$', RedirectView.as_view(url='/')),
    url('region/', region, name='region'),
    url('subcategory/', subcategory, name='subcategory'),
    url('category/', category, name='category'),
    url('size/', size, name='size'),
    url('public/', public, name='public'),
    url('login/', MyObtainTokenPairView.as_view(), name='token_obtain_pair'),
    url('login/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    url('register/normal/', register_normal_user, name='auth_register'),
    url('register/provider/', RegisterProviderUserSerializer, name='auth_register'),
]
