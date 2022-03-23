import logging

from collections import defaultdict
import datetime

from django.template.loader import render_to_string
from django.core.mail import EmailMultiAlternatives

from django.conf import settings

from apscheduler.schedulers.blocking import BlockingScheduler
from apscheduler.triggers.cron import CronTrigger
from django.core.management.base import BaseCommand
from django_apscheduler.jobstores import DjangoJobStore
from django_apscheduler.models import DjangoJobExecution

from news.models import Post

logger = logging.getLogger(__name__)

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


def send_posts_weekly():

    today = datetime.datetime.now()
    last_week = today - datetime.timedelta(days=7)
    last_week_posts_qs = Post.objects.filter(pubData__gte=last_week)

    posts_for_user = defaultdict(set)

    for post in last_week_posts_qs:
        for category in post.category.all():
            for user in category.subscribers.all():
                posts_for_user[user].add(post)

    for user, posts in posts_for_user.items():
        send_posts(user.email, posts)




def delete_old_job_executions(max_age=604_800):
    """This job deletes all apscheduler job executions older than `max_age` from the database."""
    DjangoJobExecution.objects.delete_old_job_executions(max_age)


class Command(BaseCommand):
    help = "Runs apscheduler."

    def handle(self, *args, **options):
        scheduler = BlockingScheduler(timezone=settings.TIME_ZONE)
        scheduler.add_jobstore(DjangoJobStore(), "default")

        # добавляем работу нашему задачнику
        scheduler.add_job(
        my_job,
        trigger=CronTrigger(day_of_week="Monday"),
        id = "my_job",
        max_instances = 1,
        replace_existing = True,
        )
        logger.info("Added job 'my_job'.")

        scheduler.add_job(
            delete_old_job_executions,
            trigger=CronTrigger(
                day_of_week="mon", hour="00", minute="00"
            ),
            id="delete_old_job_executions",
            max_instances=1,
            replace_existing=True,
        )
        logger.info(
            "Added weekly job: 'delete_old_job_executions'."
        )

        try:
            logger.info("Starting scheduler...")
            scheduler.start()
        except KeyboardInterrupt:
            logger.info("Stopping scheduler...")
            scheduler.shutdown()
            logger.info("Scheduler shut down successfully!")

        def my_job():
            send_mail(
             'Job mail',
             'hello from job!',
              from_email='ponialponyal@yandex.ru',
              recipient_list=['illyka@yandex.ru'],
              )
        scheduler.my_job()

