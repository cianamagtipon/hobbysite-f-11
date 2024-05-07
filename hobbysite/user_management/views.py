from .models import Profile
from .forms import ProfileForm
from django.shortcuts import render
from django.views.generic.edit import UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin


class UpdateView(LoginRequiredMixin, UpdateView):
    model = Profile
    form_class = ProfileForm
    template_name = "profile.html"
    
    def get_object(self):
        return Profile.objects.get(user=self.request.user)