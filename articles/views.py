from django.shortcuts import render
from articles.models import Article


# Detail
def detail_view(request, id):
    # from Article database
    obj = None
    if id is not None:
        obj = Article.objects.get(id=id)

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
def create_view(request):
    context = dict()
    print(request.POST)
    return render(request=request, template_name='articles/create.html', context=context)
