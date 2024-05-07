from django.shortcuts import render
from django.http import HttpResponse

from .forms import ThreadForm
from .models import Thread, ThreadCategory

from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy

def index(request):
    return HttpResponse('Welcome to Forum Threads!')


class ThreadListView(ListView):
    model = Thread
    template_name = 'thread_list.html'


class ThreadDetailView(DetailView):
    model = Thread
    template_name = 'thread_detail.html'
    

class ThreadCreateView(LoginRequiredMixin, CreateView):
    model = Thread
    form_class = ThreadForm
    template_name = "thread_create.html"
    
    def get_success_url(self):
        return reverse_lazy("forum:threads")
    

class ThreadUpdateView(LoginRequiredMixin, UpdateView):
    model = Thread
    form_class = ThreadForm
    template_name = "thread_detail.html"
    
    def get_success_url(self):
        return reverse_lazy("forum:threads")