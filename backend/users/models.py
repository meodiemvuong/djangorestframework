from django.utils import timezone
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.mail import send_mail
from django.dispatch import receiver
from django.urls import reverse
from django_rest_passwordreset.signals import reset_password_token_created
from django.core.mail import send_mail  
# Create your models here.

class User(AbstractUser):
    username = None
    first_name = None
    last_name = None
    email = models.EmailField(max_length=200 ,unique=True, null=False)
    name = models.CharField(max_length=200)
    password = models.CharField(max_length=200)
    gender = models.CharField(max_length=200)
    phone = models.CharField(max_length=200)
    createAt = models.DateField(default=timezone.now)
    REQUIRED_FIELDS = []
    USERNAME_FIELD = 'email'

    def email_user(self, subject, message, from_email=None, **kwargs):
        #Send Email to User
        send_mail(subject, message, from_email, [self.email], **kwargs)




@receiver(reset_password_token_created)
def password_reset_token_created(sender, instance, reset_password_token, *args, **kwargs):

    email_plaintext_message = "127.0.0.1:8000{}confirm/?token={}".format(reverse('password_reset:reset-password-request'), reset_password_token.key)

    send_mail(
        # title:
        "Password Reset for {title}".format(title="Backend Dev"),
        # message:
        email_plaintext_message,
        # from:
        "thanhbinh16092k1@gmail.com",
        # to:
        [reset_password_token.user.email]
    )