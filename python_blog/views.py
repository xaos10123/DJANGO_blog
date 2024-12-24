from django.shortcuts import render
from django.urls import reverse
# from python_blog.blog_data import dataset
from python_blog.models import Post
from unidecode import unidecode
from django.utils.text import slugify

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
    last_data = Post.objects.all()
    context = {
        'datax' : last_data,
        'most_liked': '',
        'categories': CATEGORIES,
        'tags': TAGS,
    }  
    return render(request, 'main.html', context=context)

def catalog_posts(request):
    context = {
        'title': 'Catalog posts',
        'name': 'Catalog posts',
        'datax': Post.objects.all(),
    }
    return render(request, 'python_blog/blog.html', context=context)

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
    data = Post.objects.all()
    context = {
        'title': f'Category detail {category_slug.title()}',
        'name': f'Category detail "{category_slug.upper()}"',
        'datails': True,
        'datax': data,
    }
    return render(request, 'python_blog/details.html', context=context)

def tag_detail(request, tag_slug):
    data = Post.objects.all()
    context = {
        'title': f'Tag detail {tag_slug.title()}',
        'name': f'Tag detail "{tag_slug.upper()}"',
        'datails': True,
        'datax': data,
    }
    return render(request, 'python_blog/details.html', context=context)


def post_detail(request, post_slug):
    datax = None
    for post in Post.objects.all():
        if post.slug == post_slug:
            datax = post
    if datax is None:
        return render(request, '404.html')
    
    
    context = {
        'datax': datax,
        'tagsx': {k: v for k, v in zip(datax.data['tags'], [slugify(unidecode(tag)) for tag in datax.data['tags']])}
    }
    return render(request, 'python_blog/post_detail.html', context=context)

def about(request):
    context = {
        'title': 'About',
        'name': 'About',
    }
    return render(request, 'about.html', context=context)