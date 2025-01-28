from django.urls import path
from python_blog import views

app_name = 'blog'

urlpatterns = [
    path('', views.catalog_posts, name='posts'),

    path('categories/<slug:category_slug>/', views.category_detail, name='category_detail'),
    path('categories/', views.catalog_categories, name='categories'),

    path('tags/<slug:tag_slug>/', views.tag_detail, name='tag_detail'),
    path('tags/', views.catalog_tags, name='tags'),

    path('post_create/', views.post_create, name='post_create'),
    path('post_update/<slug:post_slug>/', views.post_update, name='post_update'),

    path('<slug:post_slug>/', views.post_detail, name='post_detail'),


]