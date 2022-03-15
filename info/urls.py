from django.urls import path, include
from . import views


urlpatterns = [
    path("subscription", views.Subscription.as_view()),
    path("subscription/<slug:id>", views.SubscriptionDetail.as_view()),
    path("nearby", views.SubscriptionNearby.as_view()),
    path("news", views.News.as_view()),
]
