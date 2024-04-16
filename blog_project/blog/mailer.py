
from datetime import datetime
from . models import *
from django.core.mail import EmailMultiAlternatives
from django.core.mail import send_mail
from django.utils.html import strip_tags
from django.template.loader import render_to_string
from django.conf import settings

class Mailer:
    """
    Mailer
    """
    def __init__(self, **kwargs):
        self.email_id = kwargs.get('email_id', None)
        self.email_status = False
        self.notification_category = "EMAIL"
        self.email_subject = kwargs.get('subject', None)
        self.subject = kwargs.get('subject', None)
        self.type = kwargs.get("type", None)
        self.content = kwargs.get("content", None)
        self.title = kwargs.get("title", None)
        if self.type == "blog":
            self.template_name = "blog.html"


    # approve = TakeAppointment.objects.get(id=i)
    def __call__(self):
        return self.email_sender()

    def email_sender(self):
        try:
            user_instance = User.objects.get(email=self.email_id)

            if self.type == "blog":
                template_data = {
                    "email":self.email_id,
                    "user":user_instance,
                    "content": self.content,
                    "title": self.title,
                    "subject": self.subject,
                }
            html_content = render_to_string(
                self.template_name, template_data)
            text_content = strip_tags(html_content)
            msg = EmailMultiAlternatives(self.subject,
                                         text_content,
                                         settings.EMAIL_HOST_USER,
                                         [self.email_id],
                                         )
            msg.attach_alternative(html_content, "text/html")
            
        except Exception as e:
            print("ef"*100, e)
            self.reason_for_failed = str(e)
            return False