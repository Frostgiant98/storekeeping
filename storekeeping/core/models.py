from pyexpat import model
from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Store(models.Model):
    store_id = models.AutoField(primary_key=True)
    store_name = models.CharField(max_length=99)
    user = models.ForeignKey(User, on_delete=models.CASCADE , null=True)

    class Meta:
        ordering = ['store_name']

    def __str__(self) -> str:
        return self.store_name.__str__()

    def __repr__(self) -> str:
        return super().__repr__()

class Item(models.Model):
    item_id = models.AutoField(primary_key=True)
    item_name = models.CharField(max_length=99)
    entry_date = models.DateTimeField(auto_now_add=True)
    expiry_date = models.DateField(verbose_name='Expiry Date', null=True)
    quantity = models.IntegerField(verbose_name='Quantity')
    store = models.ForeignKey(Store, on_delete=models.CASCADE, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE , null=True)

    class Meta:
        ordering = ['expiry_date']

    def __str__(self) -> str:
        return self.item_name.__str__()
