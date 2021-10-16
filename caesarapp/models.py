from django.db import models
from django.utils import timezone
# Create your models here.

class UserInput(models.Model):
    plain_text = models.CharField(max_length=140)
    encryption_key = models.IntegerField(default=0)
    hill_key = models.CharField(default="abvs",max_length=140)
    pub_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.plain_text