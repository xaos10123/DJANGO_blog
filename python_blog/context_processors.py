
from django.urls import reverse


MENU_ITEMS = [
    {"title": "Главная", "url_name": 'main', 'url': str(reverse('main'))},
    {"title": "Все посты", "url_name": "blog:posts", 'url': str(reverse('blog:posts'))},
    {"title": "Категории", "url_name": "blog:categories", 'url': str(reverse('blog:categories'))},
    {"title": "Теги", "url_name": "blog:tags", 'url': str(reverse('blog:tags'))},
]



def menu_items(request):
    return {
        'menu_items': MENU_ITEMS
    }

def go_back(request):
    return request.META.get('HTTP_REFERER')