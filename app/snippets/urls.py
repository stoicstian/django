from django.urls import path
from .views import SnippetDetail, SnippetList
from rest_framework.urlpatterns import format_suffix_patterns


urlpatterns = [
    path("snippets/", SnippetList.as_view()),
    path("snippets/<int:pk>/", SnippetDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
