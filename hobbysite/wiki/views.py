from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Article, ArticleCategory, Comment
from .forms import ArticleForm, CommentForm

class ArticleListView(ListView):
    model = Article
    context_object_name = 'articles'
    template_name = 'article_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user_articles'] = Article.objects.filter(author=self.request.user) if self.request.user.is_authenticated else None
        context['categories'] = ArticleCategory.objects.prefetch_related('articles').all()
        return context

class ArticleDetailView(DetailView):
    model = Article
    template_name = 'article_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['related_articles'] = Article.objects.filter(category=self.object.category).exclude(id=self.object.id)[:2]
        context['comments'] = self.object.comments.order_by('-created_on')
        context['form'] = CommentForm()
        return context

    def post(self, request, *args, **kwargs):
        form = CommentForm(request.POST)
        if form.is_valid() and request.user.is_authenticated:
            Comment.objects.create(
                article=self.get_object(),
                author=request.user,
                entry=form.cleaned_data['entry']
            )
            return redirect(self.get_object().get_absolute_url())
        return self.get(request, *args, **kwargs)

class ArticleCreateView(LoginRequiredMixin, CreateView):
    model = Article
    form_class = ArticleForm
    template_name = 'article_form.html'
    
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('wiki:article-detail', kwargs={'pk': self.object.pk})

class ArticleUpdateView(LoginRequiredMixin, UpdateView):
    model = Article
    form_class = ArticleForm
    template_name = 'article_form.html'
    
    def get_queryset(self):
        return Article.objects.filter(author=self.request.user)

    def get_success_url(self):
        return reverse_lazy('wiki:article-detail', kwargs={'pk': self.object.pk})
