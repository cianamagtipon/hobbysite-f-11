from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from .models import Profile

from .models import Profile

class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)
    display_name = forms.CharField(max_length=63, required=False)

    class Meta:
        model = Profile  # Use Profile instead of User
        fields = ('username', 'email', 'display_name', 'password1', 'password2')

    def save(self, commit=True):
        user = super().save(commit=commit)  # No need to handle the profile separately
        return user

class LoginForm(AuthenticationForm):
    username = forms.CharField(label='Username')
    password = forms.CharField(label='Password', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('username', 'password')
