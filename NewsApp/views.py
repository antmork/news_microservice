from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.views import Response
from rest_framework import status
from NewsApp.models import News
from . serializers import NewsSerializer
'''
def news_list(request):
    news = News.objects.all()
    return render(request, "NewsApp/news_list.html", {"NewsApp": news})
'''

class NewsList(APIView):
    def get(self, request):
        News1 = News.objects.all()
        serializer = NewsSerializer(News1, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = NewsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)