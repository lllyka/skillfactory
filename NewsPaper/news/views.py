from django.shortcuts import render, redirect, reverse
from datetime import datetime
from django.views.generic import ListView, DetailView, DeleteView, TemplateView
from .models import Post, Category, Author
from .filters import PostFilter
from .forms import PostForm
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.shortcuts import redirect
from django.contrib.auth.models import Group, User
from django.contrib.auth.decorators import login_required
from django.views.generic.edit import CreateView, UpdateView
from django.core.mail import send_mail
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string  # импортируем функцию, которая срендерит наш html в текст



class PostsList(ListView):
    model = Post
    template_name = 'posts.html'
    context_object_name = 'news'
    queryset = Post.objects.order_by('-id')
    paginate_by = 1
    form_class = PostForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['time_now'] = datetime.utcnow()
        context['filter'] = PostFilter(self.request.GET, queryset=self.get_queryset())
        context['categories'] = Category.objects.all()
        context['form'] = PostForm()
        return context

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)

        if form.is_valid():
                form.save()
        return super().get(request, *args, **kwargs)


class PostDetail(DetailView):
    template_name = 'post_detail.html'
    queryset = Post.objects.all()
    context_object_name = 'news'

class PostCreate(PermissionRequiredMixin,CreateView):
    template_name = 'post_create.html'
    permission_required = ('news.add_post')
    form_class = PostForm

    def mail_post(self, request, *args, **kwargs):
        send_mail(
            subject=f'{Post.title}',
            message='Привет, новая статья в твоем разделе!',
            from_email='ponialponyal@yandex.ru',
            recipient_list=['illyka@yandex.ru']
        )

class PostUpdate(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    template_name = 'post_create.html'
    login_required = ('post_create')
    permission_required = ('news.change_post')
    form_class = PostForm


    def get_object(self, **kwargs):
        id = self.kwargs.get('pk')
        return Post.objects.get(pk=id)

class PostDelete(DeleteView):
    template_name = 'post_delete.html'
    queryset = Post.objects.all()
    success_url = '/news/'
    context_object_name = 'news'


class Search(ListView):
    model = Post
    template_name = 'search.html'
    context_object_name = 'search'
    paginate_by = 1

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter'] = PostFilter(self.request.GET, queryset=self.get_queryset())
        return context


class IndexView(LoginRequiredMixin, TemplateView):
    template_name = 'protect/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['is_not_authors'] = not self.request.user.groups.filter(name='authors').exists()
        context['is_auth'] = self.request.user.is_authenticated
        return context

class MailSend(ListView):
    def get(self, request, *args, **kwargs):
        return render(request, 'posts.html', {})

    def post_mail_for_users(self, request, *args, **kwargs):
        post_mail = Post
        html_content = render_to_string(
            'mail_created.html',)
        msg = EmailMultiAlternatives(
            subject=f'{post_mail.title} ',
            body=post_mail.text,  # это то же, что и message
            from_email='ponialponyal@yandex.ru',
            to=['illyka@yandex.ru'],  # это то же, что и recipients_list
        )
        msg.attach_alternative(html_content, "text/html")  # добавляем html

        msg.send()  # отсылаем


        return redirect('post_mail:mail_created')




@login_required
def upgrade_me(request):
    user = request.user
    authors_group = Group.objects.get(name='authors')
    if not request.user.groups.filter(name='authors').exists():
        authors_group.user_set.add(user)
    return redirect('/news/')

@login_required
def subscribed_category(request, *args, **kwargs):
    post = Post.objects.get(pk=kwargs['pk'])
    for category in post.category.all():
        user = User.objects.get(pk=request.user.id)
        if user not in category.subscribers.all():
            category.subscribers.add(user)
        else:
            category.subscribers.remove(user)
    return redirect(request.META.get('/'))
