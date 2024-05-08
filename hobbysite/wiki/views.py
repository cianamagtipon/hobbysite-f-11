from django.shortcuts import render, get_object_or_404
from django.contrib.authors.decorators import login_required
from django.db.models import Count
from .models import Article, ArticleCategory, Comment
from .forms import CommentForm

def article_list_view(request):
    if request.user.is_authenticated:
        user_articles = Article.objects.filter(author=request.user)
    else:
        user_articles = None 
    
    all_articles = Article.objects.exclude(author=request.user)
    if request.user.is_authenticated
    else Article.objects.all()

    grouped_articles = Article.objects.values('category_name').annotate(count=Count'id')

    return render(request, 'article_list.html', {'grouped_articles': grouped_articles, 'user_articles': user_articles, 
                                                'all_articles': all_articles})

def article_detail_view(request, pk):
    article = get_object_or_404(Article, pk=pk)

    related_articles = Article.objects.filter(category=article_category).excllude(pk=pk)[:2]
    comments = Comment.objects.filter(article=article).order_by('-created_on')

    if request.method =='POST': 
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.article = article
            comment.author = request.user
            comment.save()
            return redirect('article_detail.html', pk=pk)
        else:
            form = CommentForm()

    return render(request, 'article_detail.html', {'article': article, 'related_articles': related_articles,
                                                    'comments': comments, 'form': form})

def article_create_view(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST, request.FILES)
        if form.is_valid():
            article = form.save(commit=False)
            article.author = request.user
            article.save()
            return redirect('article_detail', pk=article.pk)
    else:
        form = ArticleForm()
    return render(request, 'article_create.html', {'form': form})

def article_update_view(request, pk):
    article = get_object_or_404(Article, pk=pk)
    if request.method == 'POST':
        form = ArticleForm(request.POST, request.FILES, instance=article)
        if form.is_valid():
            form.save()
            return redirect('article_detail', pk=pk)
    else:
        form = ArticleForm(instance=article)
    return render(request, 'article_update.html', {'form': form})
