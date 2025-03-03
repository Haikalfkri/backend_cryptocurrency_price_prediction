from django.db import models

# Create your models here.
class CryptoData(models.Model):
    coint_name = models.CharField(max_length=255)
    date = models.DateField()
    open_price = models.DecimalField(max_digits=10, decimal_places=2)
    high_price = models.DecimalField(max_digits=10, decimal_places=2)
    low_price = models.DecimalField(max_digits=10, decimal_places=2)
    close = models.DecimalField(max_digits=10, decimal_places=2)
    volume = models.DecimalField(max_digits=20, decimal_places=2)

    class Meta:
        db_table = 'crypto_data'
        managed = False

    def __str__(self):
        return self.coint_name