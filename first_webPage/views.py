"""Asli views.py first_webPage ichida yo'q. Biz uni qo'shimcha sifatida qo`shib oldik."""
from django.http import HttpResponse
from django.utils import timezone
from random import randint
from articles.models import Article

def home(request):
    name = 'Django'
    date = timezone.now()
    number = randint(1, 3)
    # from database
    obj = Article.objects.get(id=number)
    title = obj.title
    content = obj.content
    H1_STRING = f"""<h1>{title} (id: {obj.id})</h1>"""
    P_STRING = f"""<p>{content}</p>"""
    HTML_STRING = H1_STRING + P_STRING
    return HttpResponse(HTML_STRING)
