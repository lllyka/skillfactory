from django.core.mail import send_mail
from celery import shared_task
from django.conf import settings
from news.models import Post
from django.template.loader import render_to_string
from datetime import datetime, timedelta
from django.core.mail import EmailMultiAlternatives
from django.utils import timezone
from collections import defaultdict

@shared_task
def send_posts(email_list, posts):
    if isinstance(email_list, str):
        subscriber_list = [email_list, ]
    else:
        subscriber_list = email_list

    email_form = settings.DEFAULT_FROM_EMAIL
    subject = 'В вашей любимой категории новая статья!'
    text_message = 'В вашей любимой категории новая статья!'

    render_html_template = render_to_string('send_posts.html', {'posts': posts, 'subject': subject})

    msg = EmailMultiAlternatives(subject, text_message, email_form, list(subscriber_list))
    msg.attach_alternative(render_html_template, 'text/html')
    msg.send()


@shared_task()
def send_posts_to_email_weekly():
    week_posts = Post.objects.filter(time_post__gte=datetime.now(tz=timezone.utc) - timedelta(days=7))
    posts_for_user = defaultdict(set)

    for post in week_posts:
        for category in post.categories.all():
            for user in category.subscribers.all():
                posts_for_user[user].add(post)

    for user, posts in posts_for_user.items():
        send_posts(user.email, posts)

