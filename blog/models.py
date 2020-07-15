from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone




class Profile(models.Model):
    us = models.OneToOneField(User,null=True, default='', on_delete=models.SET_NULL)
    description = models.TextField(max_length=258)
    occupy = models.CharField(max_length=20)

    def __str__(self):
        return "{}profile".format(self.us)

class Poost(models.Model):
    us = models.ForeignKey(
        User,
        null=True,
        default='',
        on_delete=models.SET_NULL,
        related_name="meeesage_user",
    )
    title = models.CharField(max_length=25)
    blog = models.TextField(max_length=258)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date =timezone.now()
        self.save()

    def __str__(self):
        return self.title
# Create your models here.
