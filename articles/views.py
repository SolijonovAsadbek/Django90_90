from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from articles.forms import ArticleForm
from articles.models import Article


# Detail
def detail_view(request, article_id):
    # from Article database
    obj = None
    if article_id is not None:
        obj = Article.objects.get(id=article_id)

    # context
    context = {
        'object': obj
    }

    # Django Render Template
    return render(request=request, template_name='articles/detail.html', context=context)


# Search
def search_view(request):
    try:
        pk = int(request.GET.get('q'))
    except:
        pk = None

    obj = None
    if pk is not None:
        try:
            obj = Article.objects.get(id=pk)
        except:
            obj = None

    context = {
        'object': obj
    }
    return render(request=request, template_name='articles/search.html', context=context)


# Create Content
@login_required
def create_view(request):
    form = ArticleForm(request.POST or None)
    context = {
        'form': form
    }
    # print(dir(form))

    if form.is_valid():
        title = form.cleaned_data.get('title')
        content = form.cleaned_data.get('content')
        print(title, content)
        Article.objects.create(title=title, content=content)
        return redirect(to='/')
    return render(request=request, template_name='articles/create.html', context=context)
