from . import views
from django.urls import path

urlpatterns = [
    path("blogposts/", views.BlogPostListCreate.as_view(),
         name="blogpost-view-creaete")
]
