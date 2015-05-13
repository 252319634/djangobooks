from django.db import models

# Create your models here.

from django.db import models


class Book(models.Model):
    name = models.CharField(max_length=50)
    pub_date = models.DateField()