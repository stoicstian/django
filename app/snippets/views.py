from django.db.models import manager
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response


from django.http import request
from django.http.response import JsonResponse
from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer
from rest_framework.status import (
    HTTP_201_CREATED,
    HTTP_204_NO_CONTENT,
    HTTP_404_NOT_FOUND,
)
from rest_framework.views import APIView
from .models import Snippet
from .serializers import SnippetSerializer
from django.views.decorators.csrf import csrf_exempt
from rest_framework import mixins, generics


class SnippetList(generics.ListAPIView):
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer


class SnippetDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer
