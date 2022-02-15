from django.urls import path
from .views import PostsList, PostDetail, Search, PostCreate, PostUpdate, PostDelete, IndexView, upgrade_me, subscribed_category

urlpatterns = [
    path('', PostsList.as_view()),
    path('protect/', IndexView.as_view()),
    path('<int:pk>', PostDetail.as_view(), name='post_detail'),
    path('add/', PostCreate.as_view(), name='post_create'),
    path('search/', Search.as_view(), name='search'),
    path('<int:pk>/edit', PostUpdate.as_view(), name='post_update'),
    path('<int:pk>/delete', PostDelete.as_view(), name='post_delete'),
    path('protect/upgrade/', upgrade_me, name='upgrade'),
    path('subscribed/<int:pk>', subscribed_category, name='subscribed'),
]