from django.shortcuts import render, redirect
from django.contrib.auth import login
from .forms import ProfileForm, SignUpForm
from django.views.generic.edit import UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy

class ProfileUpdateView(LoginRequiredMixin, UpdateView):
    model = Profile
    form_class = ProfileForm
    template_name = "user_management/profile_update.html"
    success_url = reverse_lazy('user_management:update_profile')

    def get_object(self):
        return self.request.user  # Directly return the logged-in user

def register(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Optionally log the user in right away
            return redirect('user_management:update_profile')  # Redirect to the profile update page
    else:
        form = SignUpForm()
    return render(request, 'user_management/register.html', {'form': form})
