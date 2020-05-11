from django import forms
from .models import Article

class CreateFrom(forms.ModelForm):
    class Meta:
        model = Article
        fields=[
            'article_author',
            'title',
            'body',
            'image',
            'category'
        ]
