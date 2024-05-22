from . import views
from django.urls import path

urlpatterns = [
    path("blogposts/", views.BlogPostListCreate.as_view(),
         name="blogpost-view-creaete"),
    path("blogposts/<int:pk>/", views.BlogPostRetrieveUpdateDelete.as_view(), name="update",),
    path("blogposts/list/", views.BlogPostList.as_view(), name="list"),
]
