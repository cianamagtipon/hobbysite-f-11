from django import forms 
from .models import Profile
from django.contrib.auth.forms import UserCreationForm

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = "__all__"
        

class SignUpForm(UserCreationForm):
    class Meta:
        model = Profile
        fields = ('user', 'display_name', 'email_address', 'password1', 'password2')