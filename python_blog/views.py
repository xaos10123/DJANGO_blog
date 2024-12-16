from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponse

CATEGORIES = [
    {'slug': 'python', 'name': 'Python'},
    {'slug': 'django', 'name': 'Django'},
    {'slug': 'postgresql', 'name': 'PostgreSQL'},
    {'slug': 'docker', 'name': 'Docker'},
    {'slug': 'linux', 'name': 'Linux'},
]

def main(request):  
    context = {
        "url_posts": reverse("blog:posts"),
        "url_categories": reverse("blog:categories"),
        "url_tags": reverse("blog:tags"),
    }  
    return render(request, 'main.html', context=context)

def catalog_posts(request):
    context = {
        'title': 'Catalog posts',
        'name': 'Catalog posts',
    }
    return render(request, 'details.html', context=context)

def catalog_categories(request):
    context = {
        'title': 'Catalog categories',
        'name': 'Catalog categories',
        'categories': CATEGORIES,
    }
    return render(request, 'details.html', context=context)

def catalog_tags(request):
    context = {
        'title': 'Catalog tags',
        'name': 'Catalog tags',
    }
    return render(request, 'details.html', context=context)
