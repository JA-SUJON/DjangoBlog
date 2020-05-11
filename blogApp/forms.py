from django import forms
from .models import Article

class CreateFrom(forms.ModelForm):
    class Meta:
        model = Article
        fields=[
            'title',
            'body',
            'image',
            'category'
        ]
