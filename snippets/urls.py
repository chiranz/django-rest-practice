from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from .views import SnippetDetail, SnippetList

urlpatterns = [

    path('snippets/', SnippetList.as_view(), name='listview'),
    path('snippets/<int:pk>/', SnippetDetail.as_view(), name='detailview')

]

urlpatterns = format_suffix_patterns(urlpatterns)
