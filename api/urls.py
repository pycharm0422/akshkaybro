from django.urls import path
from .models import News
from .views import NewsList


urlpatterns = [
    path('news',NewsList.as_view()),

]