from celery import shared_task
import time
from .views import MailSend,DetailView,subscribed_category,send_mail


