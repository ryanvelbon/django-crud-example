from django.urls import reverse_lazy
from django.shortcuts import render
from django.views.generic import CreateView, ListView

from .forms import ArticleCreateForm
from .models import Article
# Create your views here.

def article_view(request, pk):
    my_context = {
        'article': Article.objects.get(pk=pk),
    }
    return render(request, 'article_read.html', context=my_context)

class ArticleCreateView(CreateView):
    form_class = ArticleCreateForm
    success_url = reverse_lazy('article-create')
    template_name = 'article_create.html'

class ArticleListView(ListView):
    model = Article
    template_name = 'home.html'
