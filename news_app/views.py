from django.shortcuts import render
from django.http import HttpRequest, HttpResponse

from .models import New


def view_news(request: HttpRequest) -> HttpResponse:
    news = New.objects.all()
    context = {
        "news": news,     
    }
    return render(request, "news/index.html", context)

