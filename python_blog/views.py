import re
from django.core.paginator import Paginator
from django.db.models import F, Q, Count
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse
from python_blog.forms import PostForm, SearchForm
from python_blog.models import Category, Post, Tag
from unidecode import unidecode
from django.utils.text import slugify


def main(request):
    posts = (
        Post.objects.select_related("category")
        .prefetch_related("tags")
        .order_by("-created_at")[:3]
    )

    context = {
        "posts": posts,
    }
    return render(request, "main.html", context=context)


def catalog_posts(request):
    forms = SearchForm(request.GET)
    q_obj = Q()

    if forms.is_valid():
        search = forms.cleaned_data.get("search")
        s_from = forms.cleaned_data.get("s_from")
        if s_from == "title":
            q_obj |= Q(title__icontains=search)
        elif s_from == "tags":
            q_obj |= Q(tags__name__icontains=search)
        else:
            q_obj |= Q(content__icontains=search)

    posts = (
        Post.objects.select_related("category")
        .prefetch_related("tags")
        .filter(q_obj)
        .order_by("-created_at")
    )
    paginator = Paginator(posts, 3)
    page_num = request.GET.get("page", 1)
    paginator = paginator.get_page(page_num)

    context = {
        "title": "Каталог постов",
        "posts": paginator,
        "posts_count": posts.count(),
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
    posts = (
        Post.objects.filter(category__slug=category_slug)
        .select_for_update("category")
        .prefetch_related("tags")
    )
    paginator = Paginator(posts, 3)
    page_num = request.GET.get("page", 1)
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
    posts = (
        Post.objects.filter(tags__slug=tag_slug)
        .select_for_update("category")
        .prefetch_related("tags")
    )
    paginator = Paginator(posts, 3)
    page_num = request.GET.get("page", 1)
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
    post = (
        Post.objects.filter(slug=post_slug)
        .select_related("category")
        .prefetch_related("tags")
        .first()
    )
    previous_page = request.META.get("HTTP_REFERER", "/")

    session = request.session
    session_key = f"post_views_{post.id}"
    if session_key not in session:
        post.views = F("views") + 1
        post.save()
        post.refresh_from_db()
        session[session_key] = True

    context = {"post": post, "previous_page": previous_page}
    return render(request, "python_blog/post_detail.html", context=context)


def about(request):
    context = {
        "title": "About",
        "name": "About",
    }
    return render(request, "about.html", context=context)


def post_create(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()

            tags = form.cleaned_data.get("tag_string", "")
            if tags:
                tag_names = [t.strip() for t in tags.split(",")]
                for tag_name in tag_names:
                    if tag_name:
                        tag, created = Tag.objects.get_or_create(
                            name=tag_name,
                            defaults={"slug": slugify(unidecode(tag_name))},
                        )
                        post.tags.add(tag)

            return redirect(post.get_absolute_url())
        context = {
            "title": "Создание поста",
            "name": "Создание поста",
            "form": form,
            "url_to": reverse("blog:post_create",),
            "category": Category.objects.all(),
            "name_form": "Создание поста",
            "button_name": "Создать",
        }
        return render(request, "python_blog/post_create.html", context=context)
    else:
        form = PostForm()
        context = {
            "title": "Создание поста",
            "name": "Создание поста",
            "form": form,
            "category": Category.objects.all(),
            "name_form": "Создание поста",
            "button_name": "Создать",
        }
        return render(request, "python_blog/post_create.html", context=context)

def post_update(request, post_slug):
    post = get_object_or_404(Post, slug=post_slug)
    if request.method == "POST":
        old_slug = post.slug
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.slug = old_slug
            post.save()

            tag_string  = form.cleaned_data.get("tag_string", "")
            if tag_string :
                post.tags.clear()
                tag_names = [t.strip() for t in tag_string .split(",")]
                for tag_name in tag_names:
                    if tag_name:
                        tag, created = Tag.objects.get_or_create(
                            name=tag_name,
                            defaults={"slug": slugify(unidecode(tag_name))},
                        )
                        post.tags.add(tag)

            return redirect(post.get_absolute_url())
    else:
        form = PostForm(instance=post)
        context = {
            "title": "Редактирование поста",
            "name": "Редактирование поста",
            "form": form,
            "category": Category.objects.all(),
            "url_to": reverse("blog:post_update", kwargs={"post_slug": post.slug}),
            "name_form": "Редактирование поста",
            "button_name": "Сохранить",
        }
        return render(request, "python_blog/post_create.html", context=context)