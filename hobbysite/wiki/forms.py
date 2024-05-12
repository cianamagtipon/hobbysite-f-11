from django import forms 
from .models import Article, Comment


class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ["title", "entry", "category"]
        
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ["entry"]
        widgets = {
            "entry": forms.Textarea(
                attrs={"cols": 80, "rows": 10}
            )
        }
