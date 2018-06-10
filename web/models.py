from django.db import models

# Create your models here.
class Cryptocurrency(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=500)
    website = models.URLField()
    twitter = models.URLField()

    def __str__(self):
        return self.name
