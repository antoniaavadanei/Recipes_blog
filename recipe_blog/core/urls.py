from django.urls import path
from . import views
from .views import HomeView,PostDetailView, CreatePostView, UpdatePostView, DeletePostView

urlpatterns = [
    # path('',views.home, name="home"),
    path('', HomeView.as_view(), name="home"),
    path('post/<int:pk>',PostDetailView.as_view(),name="post_detail"),
    path('add_post/',CreatePostView.as_view(),name="add_post"),
    path('post/edit/<int:pk>',UpdatePostView.as_view(),name="update_post"),
    path('post/<int:pk>/delete', DeletePostView.as_view(), name="delete_post"),
]

