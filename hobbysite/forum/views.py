from django.shortcuts import render
from django.http import HttpResponse
from .models import Post

from django.views.generic.list import ListView
from django.views.generic.detail import DetailView

def index(request):
    return HttpResponse('Welcome to Forums!')


class ForumListView(ListView):
    model = Post
    template_name = 'forum_list.html'


class ForumDetailView(DetailView):
    model = Post
    template_name = 'forum_detail.html'