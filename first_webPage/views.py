"""Asli views.py first_webPage ichida yo'q. Biz uni qo'shimcha sifatida qo`shib oldik."""
from django.http import HttpResponse
from django.utils import timezone
from random import randint


def home(request):
    name = 'Django'
    date = timezone.now()
    number = randint(1, 100)
    H1_STRING = f"""<h1>Hello {name}-Time: {date}</h1>"""
    P_STRING = f"""<p>Hello {number}</p>"""
    HTML_STRING = H1_STRING + P_STRING
    return HttpResponse(HTML_STRING)
