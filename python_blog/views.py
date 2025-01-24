from django.db.models import Count
from django.shortcuts import render
from django.urls import reverse
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
    posts = Post.objects.select_related('category').prefetch_related('tags').order_by("-created_at")

    context = {
        "title": "Каталог постов",
        "posts": posts,
        'posts_count': posts.count(),
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
    posts = Post.objects.all()
    data = list(
        filter(
            lambda x: category_slug == slugify(unidecode(x.data["category"].lower())),
            posts,
        )
    )
    posts_tags = {}
    for post in posts:
        posts_tags[post.slug] = {
            k: v
            for k, v in zip(
                post.data["tags"],
                [slugify(unidecode(tag)) for tag in post.data["tags"]],
            )
        }
    context = {
        "title": f"Category detail {category_slug.title()}",
        "name": f'Category detail "{category_slug.upper()}"',
        "datails": True,
        "datax": data,
        "tags": posts_tags,
    }
    print(data)
    return render(request, "python_blog/details.html", context=context)


def tag_detail(request, tag_slug):
    posts = Post.objects.all()
    data = list(
        filter(
            lambda x: tag_slug in [slugify(unidecode(tag)) for tag in x.data["tags"]],
            posts,
        )
    )
    posts_tags = {}
    for post in posts:
        posts_tags[post.slug] = {
            k: v
            for k, v in zip(
                post.data["tags"],
                [slugify(unidecode(tag)) for tag in post.data["tags"]],
            )
        }

    context = {
        "title": f"Tag detail {tag_slug.title()}",
        "name": f'Tag detail "{tag_slug.upper()}"',
        "datails": True,
        "datax": data,
        "tags": posts_tags,
    }
    return render(request, "python_blog/details.html", context=context)


def post_detail(request, post_slug):
    datax = None
    for post in Post.objects.all():
        if post.slug == post_slug:
            datax = post
    if datax is None:
        return render(request, "404.html")

    context = {
        "datax": datax,
        "tagsx": {
            k: v
            for k, v in zip(
                datax.data["tags"],
                [slugify(unidecode(tag)) for tag in datax.data["tags"]],
            )
        },
    }
    return render(request, "python_blog/post_detail.html", context=context)


def about(request):
    context = {
        "title": "About",
        "name": "About",
    }
    return render(request, "about.html", context=context)
