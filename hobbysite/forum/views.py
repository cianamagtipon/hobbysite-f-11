from django.shortcuts import render
from django.http import HttpResponse
from .models import Thread

from django.views.generic.list import ListView
from django.views.generic.detail import DetailView

def index(request):
    return HttpResponse('Welcome to Forum Threads!')


class ForumListView(ListView):
    model = Thread
    template_name = 'forum_list.html'


class ForumDetailView(DetailView):
    model = Thread
    template_name = 'forum_detail.html'