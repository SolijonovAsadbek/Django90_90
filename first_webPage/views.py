"""Asli views.py first_webPage ichida yo'q. Biz uni qo'shimcha sifatida qo`shib oldik."""
from django.http import HttpResponse
from django.utils import timezone
from random import randint
from articles.models import Article
from django.template.loader import render_to_string


def home(request):
    name = 'Django'
    date = timezone.now()
    number = randint(1, 3)
    # from database
    obj = Article.objects.get(id=number)

    # context
    context = {'title': obj.title,
               'id': obj.id,
               'content': obj.content}
    # Django templates
    HTML_STRING = render_to_string(template_name='home.html', context=context)

    return HttpResponse(HTML_STRING)
