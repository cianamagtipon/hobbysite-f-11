from django import forms
from .models import Article, Comment

class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ['title', 'category', 'entry', 'header_image']  # Assuming 'header_image' is part of your Article model as mentioned in specs

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['entry']
