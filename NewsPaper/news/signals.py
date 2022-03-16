from django.dispatch import receiver
from django.db.models.signals import post_save,  m2m_changed
from django.core.mail import EmailMultiAlternatives
from django.conf import settings
from django.template.loader import render_to_string
from .models import Post, Category

@receiver(post_save, sender=Post)
def save_post(created, **kwargs):
    post_turn = kwargs['instance']
    subscribers_list = {user.email
                        for category in post_turn.category.all()
                        for user in category.subscribers.all()}
    email_from = settings.DEFAULT_FROM_EMAIL

    if created:
        subject = 'В вашей любимой категории новая статья!'
        text_message = f'В вашей любимой категории новая статья:'
    else:
        subject = 'В категориях, на которые вы подписаны, была изменена статья'
        text_message = f'В категориях, на которые вы подписаны,была изменена статья:'
    html_template = render_to_string('send_mail.html', {'post': post_turn, 'subject': subject})

    msg = EmailMultiAlternatives(subject, text_message, email_from, list(subscribers_list))
    msg.attach_alternative(html_template, 'text/html')
    msg.send()


@receiver(m2m_changed, sender=Post.category.through)
def notify_managers_post(instance, action, pk_set, *args, **kwargs):
    if action == 'post_add':
        html_content = render_to_string(
            'mail_created.html',
            {'post': instance,
             }
        )
        for pk in pk_set:
            category = Category.objects.get(pk=pk)
            recipients = [user.email for user in category.subscribers.all()]
            msg = EmailMultiAlternatives(
                subject=f'На сайте NewsPaper новая статья: {instance.title}',

                from_email=settings.DEFAULT_FROM_EMAIL,
                to=recipients
            )
            msg.attach_alternative(html_content, "text/html",)
            msg.send()