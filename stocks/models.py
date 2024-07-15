from django.db import models

# Create your models here.
class Stock(models.Model):
    name = models.CharField(max_length=100)
    ev = models.FloatField()
    ebitda = models.FloatField()
    ev_ebitda = models.FloatField()
    roe = models.FloatField()
    roa = models.FloatField()
    pe = models.FloatField()
    pbv = models.FloatField()

    def __str__(self):
        return self.name