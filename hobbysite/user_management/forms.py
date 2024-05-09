from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Profile

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['display_name', 'email']  # Specify fields to be included in the form

class SignUpForm(UserCreationForm):
    class Meta:
        model = Profile
        fields = ('username', 'display_name', 'email', 'password1', 'password2')
