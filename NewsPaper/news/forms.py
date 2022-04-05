from allauth.account import forms
from django.forms import ModelForm, Form, HiddenInput
from .models import Post
from allauth.account.forms import SignupForm
from django.contrib.auth.models import Group


class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = ['author', 'text', 'category', 'title']

    """widgets = {
        'author': forms.HiddenInput(),
    }"""
class CommonSignupForm(SignupForm):

    def save(self, request):
        user = super(CommonSignupForm, self).save(request)
        common_group = Group.objects.get(name='common')
        common_group.user_set.add(user)
        return user