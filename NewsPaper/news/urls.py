from django.urls import path
from .views import PostsList, PostDetail, Search , PostCreate, PostUpdate, PostDelete# импортируем наше представление

urlpatterns = [
    path('', PostsList.as_view()),
    path('', PostDetail.as_view(), name = 'post_detail'),
    path('add/', PostCreate.as_view(), name='post_create'),
    path('search', Search.as_view(), name = 'search'),
    path('/news/<int:pk>/edit', PostUpdate.as_view(), name='post_update'),
    path('/news/<int:pk>/delete', PostDelete.as_view(), name='post_delete'),
]