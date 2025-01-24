from django.core.paginator import Paginator
from django.db.models import F, Q, Count
from django.shortcuts import render
from django.urls import reverse
from python_blog.forms import SearchForm
from python_blog.models import Category, Post, Tag
from unidecode import unidecode
from django.utils.text import slugify


def main(request):
    posts = Post.objects.select_related('category').prefetch_related('tags').order_by("-created_at")[:3]
    
    context = {
        "posts": posts,        
    }
    return render(request, "main.html", context=context)


def catalog_posts(request):
    forms = SearchForm(request.GET)
    q_obj = Q()

    if forms.is_valid():
        search = forms.cleaned_data.get('search')
        s_from = forms.cleaned_data.get('s_from')
        if s_from=='title':
            q_obj |= Q(title__icontains=search)
        elif s_from=='tags':
            q_obj |= Q(tags__name__icontains=search)
        else:
            q_obj |= Q(content__icontains=search)
    

    posts = Post.objects.select_related('category').prefetch_related('tags').filter(q_obj).order_by("-created_at")
    paginator = Paginator(posts, 3)
    page_num = request.GET.get('page', 1)
    paginator = paginator.get_page(page_num)
            

    context = {
        "title": "Каталог постов",
        "posts": paginator,
        'posts_count': posts.count(),
        "form": forms,
    }

    return render(request, "python_blog/blog.html", context=context)


def catalog_categories(request):
    categories = Category.objects.all()

    context = {
        "title": "Категории",
        "name": "Категории",
        "data": categories,
        "count": categories.count(),
    }
    return render(request, "python_blog/details.html", context=context)


def catalog_tags(request):
    tags = Tag.objects.all()

    context = {
        "title": "Тэги",
        "name": "Тэги",
        "data": tags,
        "count": tags.count(),
    }
    return render(request, "python_blog/details.html", context=context)


def category_detail(request, category_slug):
    posts = Post.objects.filter(category__slug=category_slug).select_for_update('category').prefetch_related('tags')
    paginator = Paginator(posts, 3)
    page_num = request.GET.get('page', 1)
    paginator = paginator.get_page(page_num)
    
    context = {
        "title": f"Категория {category_slug.title()}",
        "name": f'Категория "{category_slug.upper()}"',
        "datails": True,
        "posts": paginator,
        "count": posts.count(),
    }
    return render(request, "python_blog/details.html", context=context)


def tag_detail(request, tag_slug):
    posts = Post.objects.filter(tags__slug=tag_slug).select_for_update('category').prefetch_related('tags')
    paginator = Paginator(posts, 3)
    page_num = request.GET.get('page', 1)
    paginator = paginator.get_page(page_num)
    
    context = {
        "title": f"Категория {tag_slug.title()}",
        "name": f'Категория "{tag_slug.upper()}"',
        "datails": True,
        "posts": paginator,
        "count": posts.count(),
    }
    return render(request, "python_blog/details.html", context=context)


def post_detail(request, post_slug):
    post = Post.objects.filter(slug=post_slug).select_related('category').prefetch_related('tags').first()
    previous_page = request.META.get('HTTP_REFERER', '/')

    session = request.session
    session_key = f"post_views_{post.id}"
    if session_key not in session:
        post.views = F('views') + 1
        post.save()
        post.refresh_from_db()
        session[session_key] = True


    context = {
        "post": post,
        "previous_page": previous_page
    }
    return render(request, "python_blog/post_detail.html", context=context)


def about(request):
    context = {
        "title": "About",
        "name": "About",
    }
    return render(request, "about.html", context=context)
