from django.db import models


# Create your models here.
class Publisher(models.Model):
    name = models.CharField(max_length=50)
    website = models.URLField()
    email = models.EmailField()

def __str__(self):
    return self.name