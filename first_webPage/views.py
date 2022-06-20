"""Asli views.py first_webPage ichida yo'q. Biz uni qo'shimcha sifatida qo`shib oldik."""
from django.http import HttpResponse

HTML_WEB_VIEW = """
Welcome to the Django Web Framework!
I work together with a Python Programming Language."""


def home(request):
    print(HTML_WEB_VIEW)
    return HttpResponse(HTML_WEB_VIEW)
