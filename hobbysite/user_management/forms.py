from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Profile

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['display_name', 'email']  # Specify which fields should be included in the form

class SignUpForm(UserCreationForm):
    class Meta:
        model = Profile
        fields = ('username', 'email', 'display_name', 'password1', 'password2')
