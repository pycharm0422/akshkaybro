from django.shortcuts import render
from .serializers import NewsSerializer
from rest_framework.generics import ListAPIView
from .models import News

class NewsList(ListAPIView):
    queryset = News.objects.all()
    serializer_class = NewsSerializer
