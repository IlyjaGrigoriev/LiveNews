from django.urls import path
from .views import view_news


app_name = "news"

urlpatterns = [
  path("", view_news, name="news")
]