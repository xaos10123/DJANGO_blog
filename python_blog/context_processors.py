MENU_ITEMS = [
    {"title": "Главная", "url_name": "main"},
    {"title": "Все посты", "url_name": "blog:posts"},
    {"title": "Категории", "url_name": "blog:categories"},
    {"title": "Теги", "url_name": "blog:tags"},
]



def menu_items(request):
    return {
        'menu_items': MENU_ITEMS
    }