from django import forms 
from .models import Thread, Comment


class ThreadForm(forms.ModelForm):
    class Meta:
        model = Thread
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