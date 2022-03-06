from django.urls import path, include
from . import views


urlpatterns = [
    path("subscription", views.Subscription.as_view()),
    path("news", views.News.as_view()),
]
