from django.urls import path, include
from . import views


urlpatterns = [
    path("subscription", views.Subscription.as_view()),
    path("subscription/<slug:id>", views.getDetail),
    path("nearby", views.nearby),
    path("news", views.News.as_view()),
]
