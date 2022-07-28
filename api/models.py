from django.db import models

# Create your models here.
class Champion(models.Model):
    name = models.CharField(max_length=50)
    sex = models.CharField(max_length=20)
    clan = models.CharField(max_length=20)