from django.urls import path
from python_blog import views

app_name = 'blog'

urlpatterns = [
    path('', views.catalog_posts, name='posts'),
    path('categories/', views.catalog_categories, name='categories'),
    path('tags/', views.catalog_tags, name='tags'),
]