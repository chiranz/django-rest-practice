from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from .views import SnippetDetail, SnippetList, UserList, UserDetail

urlpatterns = [

    path('snippets/', SnippetList.as_view(), name='listview'),
    path('snippets/<int:pk>/', SnippetDetail.as_view(), name='detailview'),
    path('user/', UserList.as_view()),
    path('user/<int:pk>/', UserDetail.as_view())

]

urlpatterns = format_suffix_patterns(urlpatterns)
