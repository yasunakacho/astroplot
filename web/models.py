from django.db import models

# Create your models here.
class Cryptocurrency(models.Model):
    name = models.CharField(max_length=20)
    description = models.CharField(max_length=400)
    website = models.URLField()
    twitter = models.URLField()

    def __str__(self):
        return self.name
