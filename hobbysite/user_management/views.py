from .models import Profile
from .forms import ProfileForm, SignUpForm
from django.shortcuts import render, redirect
from django.views.generic.edit import UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import login


class UpdateView(LoginRequiredMixin, UpdateView):
    model = Profile
    form_class = ProfileForm
    template_name = "profile.html"
    
    def get_object(self):
        return Profile.objects.get(user=self.request.user)
    
def register(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Log the user in directly after registration
            return redirect('homepage')  # Redirect to homepage or other appropriate page
    else:
        form = SignUpForm()
    return render(request, 'user_management/register.html', {'form': form})