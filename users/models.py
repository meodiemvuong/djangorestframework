from django.utils import timezone
from django.db import models
from django.contrib.auth.models import AbstractUser
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