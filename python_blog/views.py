from django.shortcuts import render
from django.urls import reverse

CATEGORIES = [
    {'slug': 'python', 'name': 'Python'},
    {'slug': 'django', 'name': 'Django'},
    {'slug': 'postgresql', 'name': 'PostgreSQL'},
    {'slug': 'docker', 'name': 'Docker'},
    {'slug': 'linux', 'name': 'Linux'},
]
TAGS = [
    {'slug': 'python', 'name': 'TAG Python'},
    {'slug': 'django', 'name': 'TAG Django'},
    {'slug': 'postgresql', 'name': 'TAG PostgreSQL'},
    {'slug': 'docker', 'name': 'TAG Docker'},
    {'slug': 'linux', 'name': 'TAG Linux'},
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
    return render(request, 'python_blog/details.html', context=context)

def catalog_categories(request):
    context = {
        'title': 'Catalog categories',
        'name': 'Catalog categories',
        'data': CATEGORIES,
    }
    return render(request, 'python_blog/details.html', context=context)

def catalog_tags(request):
    context = {
        'title': 'Catalog tags',
        'name': 'Catalog tags',
        'data': TAGS,
    }
    return render(request, 'python_blog/details.html', context=context)


def category_detail(request, category_slug):
    context = {
        'title': f'Category detail {category_slug.title()}',
        'name': f'Category detail "{category_slug.upper()}"',
        'data': None,
    }
    return render(request, 'python_blog/details.html', context=context)

def tag_detail(request, tag_slug):
    context = {
        'title': f'Tag detail {tag_slug.title()}',
        'name': f'Tag detail "{tag_slug.upper()}"',
        'data': None,
    }
    return render(request, 'python_blog/details.html', context=context)


def post_detail(request, post_slug):
    context = {
        'title': f'Post detail {post_slug.title()}',
        'name': f'Post detail "{post_slug.upper()}"',
    }
    return render(request, 'python_blog/post_detail.html', context=context)

def about(request):
    context = {
        'title': 'About',
        'name': 'About',
    }
    return render(request, 'about.html', context=context)