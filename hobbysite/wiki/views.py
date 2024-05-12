

class ArticleDetailView(DetailView):
    model = Article
    form_class = CommentForm
    template_name = 'article_detail.html'

    def get(self, request, *args, **kwargs):
        article = self.get_object()
        related_articles = Article.objects.filter(category=article.category)
        form = self.form_class()
        return render(request, self.template_name, 
                      {"article": article, 
                       "related_articles": related_articles, 
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
