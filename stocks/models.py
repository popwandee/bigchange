from django.db import models

# Create your models here.
from django.db import models

class Stock(models.Model):
    symbol = models.CharField(max_length=10, default='a')
    price = models.FloatField(default=0)
    market_cap = models.FloatField(default=0)
    ev = models.FloatField(default=0)
    ev_ebitda = models.FloatField(default=0)
    pe_ratio = models.FloatField(default=0)
    pbv_ratio = models.FloatField(default=0)
    roe = models.FloatField(default=0)
    roa = models.FloatField(default=0)
    de_ratio = models.FloatField(default=0)

    def __str__(self):
        return self.symbol