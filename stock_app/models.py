from django.db import models

# Create your models here.
# stock_app/models.py

class Stock(models.Model):
    name = models.CharField(max_length=100)
    ev = models.FloatField()  # Enterprise Value
    ebitda = models.FloatField()  # Earnings Before Interest, Taxes, Depreciation, and Amortization
    ev_ebitda = models.FloatField()
    detail = models.TextField()

    def ev_ebitda_ratio(self):
        return self.ev / self.ebitda

    def __str__(self):
        return self.name
