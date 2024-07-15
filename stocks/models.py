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
    
class StockCSV(models.Model):
    file = models.FileField(upload_to='csvs/')
    uploaded_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.file.name