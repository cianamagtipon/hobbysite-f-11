from django.shortcuts import render
from django.http import HttpResponse

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
    # http_method_names = ["get", "post"]
    model = Thread
    form_class = CommentForm
    template_name = 'thread_detail.html'

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx['comments'] = Comment.objects.all()
        ctx['form'] = CommentForm()
        return ctx
    
    def post(self, request, *args, **kwargs):
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = Comment()
            comment.entry = form.cleaned_data.get('entry')
            comment.save()
            return self.get(request, *args, **kwargs)
        else: 
            self.object_list = self.get_queryset(**kwargs)
            context = self.get_context_data(**kwargs)
            context["form"] = form
            return self.render_to_response(context)
    
    # def form_valid(self, form):
    #     return super().form_valid(form)    
    
    # def get_success_url(self):
    #     return self.model.get_absolute_url()

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