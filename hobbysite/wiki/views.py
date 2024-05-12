from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect

from .forms import ArticleForm, CommentForm
from .models import Article, Comment

from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy

def index(request):
    return HttpResponse('Welcome to Wiki!')


class ArticleListView(ListView):
    model = Article
    template_name = 'article_list.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.request.user
        if user.is_authenticated:
            context['user_articles'] = Article.objects.filter(author=user.profile)
            context['all_articles'] = Article.objects.exclude(author=user.profile)
        else:
            context['user_articles'] = None
            context['all_articles'] = Article.objects.all()
        return context


class ArticleDetailView(DetailView):
    model = Article
    form_class = CommentForm
    template_name = 'article_detail.html'

    def get(self, request, *args, **kwargs):
        article = self.get_object()
        other_articles = Article.objects.filter(category=article.category)
        form = self.form_class()
        return render(request, self.template_name, 
                      {"article": article, 
                       "other_articles": other_articles, 
                       "form": form})    
    
    def post(self, request, *args, **kwargs):
        article = self.get_object()
        form = self.form_class(request.POST)
        user = self.request.user
        if user.is_authenticated:
            author = user.profile
        else:
            author = None

        if form.is_valid():
            comment = Comment()
            comment.article = article
            comment.author = author
            comment.entry = form.cleaned_data.get('entry')
            comment.save()
        return HttpResponseRedirect(self.request.path)


class ArticleCreateView(LoginRequiredMixin, CreateView):
    model = Article
    form_class = ArticleForm
    template_name = "article_create.html"
    
    def get_success_url(self):
        return reverse_lazy("wiki:articles")

    def form_valid(self, form):
        if self.request.user.is_authenticated:
            form.instance.author = self.request.user.profile
        return super().form_valid(form)    

class ArticleUpdateView(LoginRequiredMixin, UpdateView):
    model = Article
    form_class = ArticleForm
    template_name = "article_update.html"
    
    def get_success_url(self):
        return reverse_lazy("wiki:articles")