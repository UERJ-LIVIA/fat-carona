from django.db import models

import datetime

# Create your models here.
class Example(models.Model):
    text = models.TextField(blank=True)
    pub_date = models.DateTimeField(default=datetime.datetime.now)