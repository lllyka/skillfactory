from django.shortcuts import render
from django.views.generic import ListView, DetailView, UpdateView, CreateView, DeleteView, TemplateView
from django.core.paginator import Paginator
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Product, Category
from .filters import ProductFilter
from .forms import ProductForm  # импортируем нашу форму


class Products(ListView):
    model = Product
    template_name = 'products.html'
    context_object_name = 'products'
    ordering = ['-price']
    paginate_by = 1

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter'] = ProductFilter(self.request.GET, queryset=self.get_queryset())
        return context



# создаём представление, в котором будут детали конкретного отдельного товара
class ProductDetailView(DetailView):
    template_name = 'product_detail.html'  # название шаблона будет product.html
    queryset = Product.objects.all()


# дженерик для создания объекта. Надо указать только имя шаблона и класс формы, который мы написали в прошлом юните. Остальное он сделает за вас
class ProductCreateView(CreateView):
    template_name = 'product_create.html'
    form_class = ProductForm


# дженерик для редактирования объекта
class ProductUpdateView(UpdateView):
    template_name = 'product_create.html'
    form_class = ProductForm

    # метод get_object мы используем вместо queryset, чтобы получить информацию об объекте, который мы собираемся редактировать
    def get_object(self, **kwargs):
        id = self.kwargs.get('pk')
        return Product.objects.get(pk=id)


# дженерик для удаления товара
class ProductDeleteView(DeleteView):
    template_name = 'product_delete.html'
    queryset = Product.objects.all()
    success_url = '/products/'


class ProtectedView(LoginRequiredMixin, TemplateView):
    template_name = 'prodected_page.html'