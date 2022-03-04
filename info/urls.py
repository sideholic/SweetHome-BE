from django.urls import path, include
from .views import getSubscriptions, postNews


urlpatterns = [
    path("subscription/", getSubscriptions),
    path("news", postNews),
]
