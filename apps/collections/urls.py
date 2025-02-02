from django.urls import path

from .views import collections

urlpatterns = [
    path('', collections, name='collections-list'),
]
