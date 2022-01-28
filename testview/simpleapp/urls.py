from django.urls import path
from .views import Products, ProductDetailView, ProductCreateView, ProductUpdateView, ProductDeleteView

urlpatterns = [
    # path означает "путь". В данном случае путь ко всем товарам у нас останется пустым, позже станет ясно, почему
    path('', Products.as_view()),
    # т. к. сам по себе это класс, то нам надо представить этот класс в виде view. Для этого вызываем метод as_view
    path('<int:pk>/', ProductDetailView.as_view(), name='product_detail'),  # Ссылка на детали товара
    path('create/', ProductCreateView.as_view(), name='product_create'),  # Ссылка на создание товара
    path('create/<int:pk>', ProductUpdateView.as_view(), name='product_update'),
    path('delete/<int:pk>', ProductDeleteView.as_view(), name='product_delete'),

]