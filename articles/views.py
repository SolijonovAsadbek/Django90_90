from django.shortcuts import render
from articles.models import Article


# Create your views here.
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
