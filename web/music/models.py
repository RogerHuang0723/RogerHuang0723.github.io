from django.db import models

# Create your models here.
from django.utils import timezone

class Member(models.Model):
    USER_ID = models.CharField(max_length=100)
    USER_PASS = models.CharField(max_length=100)
    USER_NAME = models.TextField()
    CREATE_DATE= models.DateTimeField(default=timezone.now)
    objects = models.Manager()
    def __str__(self):
        return self.USER_NAME