from django.urls import path
from .views import Products, ProductDetailView, ProductCreateView, ProductUpdateView, ProductDeleteView
from django.contrib import admin
from django.urls import include
from django.urls import path
from .views import IndexView
from .views import upgrade_me



urlpatterns = [
    # path означает "путь". В данном случае путь ко всем товарам у нас останется пустым, позже станет ясно, почему
    path('', Products.as_view()),
    # т. к. сам по себе это класс, то нам надо представить этот класс в виде view. Для этого вызываем метод as_view
    path('<int:pk>/', ProductDetailView.as_view(), name='product_detail'),  # Ссылка на детали товара
    path('create/', ProductCreateView.as_view(), name='product_create'),  # Ссылка на создание товара
    path('create/<int:pk>', ProductUpdateView.as_view(), name='product_update'),
    path('delete/<int:pk>', ProductDeleteView.as_view(), name='product_delete'),
    path('accounts/', IndexView.as_view()),
    path('upgrade/', upgrade_me, name = 'upgrade'),

]
