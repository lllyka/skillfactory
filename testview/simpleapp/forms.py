from django.forms import ModelForm, BooleanField  # Импортируем true-false поле
from .models import Product
from allauth.account.forms import SignupForm
from django.contrib.auth.models import Group
from allauth.account import forms
from django.forms import ModelForm, Form, HiddenInput
from .models import Product
from allauth.account.forms import SignupForm
from django.contrib.auth.models import Group


class ProductForm(ModelForm):
    check_box = BooleanField(label='Ало, Галочка!')  # добавляем галочку, или же true-false поле

    class Meta:
        model = Product
        fields = ['name', 'price', 'category', 'quantity',
                  'check_box']  # не забываем включить галочку в поля, иначе она не будет показываться на странице!


class BasicSignupForm(SignupForm):

    def save(self, request):
        user = super(BasicSignupForm, self).save(request)
        basic_group = Group.objects.get(name='basic')
        basic_group.user_set.add(user)
        return user