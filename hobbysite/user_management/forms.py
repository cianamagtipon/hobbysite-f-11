from django import forms 
from .models import Profile

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = "__all__"
        widgets = {
            "due_date":forms.TextInput(
                attrs={"type": "datetime-local"}
            )
        }