from django.urls import path
from . import views
from .views import HomeView,PostDetailView, CreatePostView, UpdatePostView, DeletePostView, CreateCategoryView, CategoryView, \
    CategoryListView, CategoryDetailView,LikeView

urlpatterns = [
    # path('',views.home, name="home"),
    path('', HomeView.as_view(), name="home"),
    path('post/<int:pk>',PostDetailView.as_view(),name="post_detail"),
    path('add_post/',CreatePostView.as_view(),name="add_post"),
    path('post/edit/<int:pk>',UpdatePostView.as_view(),name="update_post"),
    path('post/<int:pk>/delete', DeletePostView.as_view(), name="delete_post"),
    path('add_category/',CreateCategoryView.as_view(),name="add_category"),
    path('category/<str:cats>/',CategoryView, name='category'),
    path('category-list/',CategoryListView, name='category-list'),
    path('category-detail/',CategoryDetailView.as_view(), name='category-detail'),
    path('like/<int:pk>',LikeView, name='like_post'),
]

