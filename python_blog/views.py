from django.shortcuts import render
from django.urls import reverse
from python_blog.blog_data import dataset

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
    data = dataset[:3]
    context = {
        'data' : data,
        'categories': CATEGORIES,
        'tags': TAGS,
    }  
    return render(request, 'main.html', context=context)

def catalog_posts(request):
    context = {
        'title': 'Catalog posts',
        'name': 'Catalog posts',
        'data': dataset,
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
    data = [datax for datax in dataset if category_slug.lower() in datax['hashtags']]
    context = {
        'title': f'Category detail {category_slug.title()}',
        'name': f'Category detail "{category_slug.upper()}"',
        'datails': True,
        'data': data,
    }
    return render(request, 'python_blog/details.html', context=context)

def tag_detail(request, tag_slug):
    data = [datax for datax in dataset if tag_slug.lower() in datax['hashtags']]
    context = {
        'title': f'Tag detail {tag_slug.title()}',
        'name': f'Tag detail "{tag_slug.upper()}"',
        'datails': True,
        'data': data,
    }
    return render(request, 'python_blog/details.html', context=context)


def post_detail(request, post_slug):
    data = None
    for post in dataset:
        if post['slug'] == post_slug:
            data = post
    if data is None:
        return render(request, '404.html')
    
    
    context = {
        'data': data,
    }
    return render(request, 'python_blog/post_detail.html', context=context)

def about(request):
    context = {
        'title': 'About',
        'name': 'About',
    }
    return render(request, 'about.html', context=context)