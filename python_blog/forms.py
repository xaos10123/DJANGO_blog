from pyexpat import model
from django import forms
from django.forms import widgets

from python_blog.models import Category, Post

class SearchForm(forms.Form):
    search = forms.CharField(max_length=100, required=False)
    s_from = forms.CharField(max_length=100, required=False)

class PostForm(forms.ModelForm):
    model = Post
    fields = ['title', 'content', 'category', 'tags']
    widgets  = {
        'title': forms.TextInput(attrs={'class': 'form-control'}),
        'content': forms.Textarea(attrs={'class': 'form-control'}),
        'category': forms.Select(attrs={'class': 'form-control'}, choices=Category.objects.all()),
        'tags': forms.Textarea(attrs={'class': 'form-control'}),
    }

    class Meta:
        model = Post
        fields = ['title', 'content', 'category', 'tags']