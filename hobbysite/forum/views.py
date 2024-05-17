from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Thread, Comment
from .forms import ThreadForm, CommentForm

def index(request):
    return HttpResponse('Welcome to Forum Threads!')

class ThreadListView(ListView):
    model = Thread
    template_name = 'thread_list.html'
    context_object_name = 'all_threads'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.request.user
        if user.is_authenticated:
            user_threads = Thread.objects.filter(author=user)
            context['user_threads'] = user_threads
            context['all_threads'] = Thread.objects.exclude(author=user)
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
        return render(request, self.template_name, {
            "thread": thread,
            "other_threads": other_threads,
            "form": form
        })

    def post(self, request, *args, **kwargs):
        thread = self.get_object()
        form = self.form_class(request.POST)
        user = request.user
        author = user if user.is_authenticated else None

        if form.is_valid():
            comment = Comment()
            comment.thread = thread
            comment.author = author
            comment.entry = form.cleaned_data['entry']
            comment.save()
        return HttpResponseRedirect(request.path)

class ThreadCreateView(LoginRequiredMixin, CreateView):
    model = Thread
    form_class = ThreadForm
    template_name = "thread_create.html"

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy("forum:threads")

class ThreadUpdateView(LoginRequiredMixin, UpdateView):
    model = Thread
    form_class = ThreadForm
    template_name = "thread_update.html"

    def get_queryset(self):
        return Thread.objects.filter(author=self.request.user)

    def get_success_url(self):
        return reverse_lazy("forum:threads")
