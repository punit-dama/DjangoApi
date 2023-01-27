from django.db import models


class Order_details(models.Model):
    order_id = models.IntegerField()
    order_amount = models.DecimalField(max_digits=10, decimal_places=2)
    payment_url = models.URLField(blank=True)
    status = models.CharField(max_length=50, default="Pending")

