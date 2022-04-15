from django.urls import path, include
from django.conf.urls import url
from .views import home_view, analysis_view

urlpatterns = [
    path('', home_view, name='home'),
    path('analysis/', analysis_view, name='analysis'),
    url(r"^oauth/", include("social_django.urls", namespace="social")),
]