from django.urls import path
from .views import PostsList, PostDetail, Search, PostCreate, PostUpdate, PostDelete, IndexView, upgrade_me, subscribe
from django.views.decorators.cache import cache_page


urlpatterns = [
    path('', cache_page(60*5)(PostsList.as_view())),
    path('protect/', IndexView.as_view()),
    path('<int:pk>', (PostDetail.as_view()), name='post_detail'),
    path('add/', cache_page(60*5)(PostCreate.as_view()), name='post_create'),
    path('search/', Search.as_view(), name='search'),
    path('<int:pk>/edit', cache_page(60*5)(PostUpdate.as_view()), name='post_update'),
    path('<int:pk>/delete', PostDelete.as_view(), name='post_delete'),
    path('protect/upgrade/', upgrade_me, name='upgrade'),
    path('subscribe/<int:pk>', subscribe, name='subscribe'),
]