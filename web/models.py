from django.db import models
from django.core.validators import MinValueValidator
from django.contrib.auth.models import User

# Create your models here.
class Cryptocurrency(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=500)
    website = models.URLField()
    twitter = models.URLField()

    def __str__(self):
        return self.name

class Price(models.Model):
    coin = models.ForeignKey(Cryptocurrency, on_delete=models.CASCADE)
    date = models.DateField()
    open = models.DecimalField(max_digits=10, decimal_places=2, validators=[MinValueValidator(0.01)])
    high = models.DecimalField(max_digits=10, decimal_places=2, validators=[MinValueValidator(0.01)])
    low = models.DecimalField(max_digits=10, decimal_places=2, validators=[MinValueValidator(0.01)])
    close = models.DecimalField(max_digits=10, decimal_places=2, validators=[MinValueValidator(0.01)])
    volume = models.CharField(max_length=100)
    marketcap = models.CharField(max_length=100)

    class Meta:
        unique_together=(("coin","date"))

    def __str__(self):
        #price_data = []
        #price_data = [str(self.coin), str(self.date), str(self.open)]
        #return price_data
        #return str(price_data)
        #return '%s %s'%(self.coin, self.date, self.open)
        return str(self.open)

class Alert(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    coin = models.ForeignKey(Cryptocurrency, on_delete=models.CASCADE)
    high_price = models.IntegerField()
    low_price  = models.IntegerField()

    def __str__(self):
        return self.coin
