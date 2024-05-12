from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect

from .forms import ThreadForm, CommentForm
from .models import Thread, Comment

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
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.request.user
        if user.is_authenticated:
            context['user_threads'] = Thread.objects.filter(author=user.profile)
            context['all_threads'] = Thread.objects.exclude(author=user.profile)
        else:
            context['user_threads'] = None
            context['all_threads'] = Thread.objects.all()
        return context


class ThreadDetailView(DetailView):
    model = Thread
    form_class = CommentForm
    template_name = 'thread_detail.html'

    def get(self, request, *args, **kwargs):
        thread = self.get_object()
        other_threads = Thread.objects.filter(category=thread.category)
        form = self.form_class()
        return render(request, self.template_name, 
                      {"thread": thread, 
                       "other_threads": other_threads, 
                       "form": form})    
    
    def post(self, request, *args, **kwargs):
        thread = self.get_object()
        form = self.form_class(request.POST)
        user = self.request.user
        if user.is_authenticated:
            author = user.profile
        else:
            author = None

        if form.is_valid():
            comment = Comment()
            comment.thread = thread
            comment.author = author
            comment.entry = form.cleaned_data.get('entry')
            comment.save()
        return HttpResponseRedirect(self.request.path)


class ThreadCreateView(LoginRequiredMixin, CreateView):
    model = Thread
    form_class = ThreadForm
    template_name = "thread_create.html"
    
    def get_success_url(self):
        return reverse_lazy("forum:threads")

    def form_valid(self, form):
        if self.request.user.is_authenticated:
            form.instance.author = self.request.user.profile
        return super().form_valid(form)    

class ThreadUpdateView(LoginRequiredMixin, UpdateView):
    model = Thread
    form_class = ThreadForm
    template_name = "thread_update.html"
    
    def get_success_url(self):
        return reverse_lazy("forum:threads")