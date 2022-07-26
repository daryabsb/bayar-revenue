from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Item(models.Model):
    CURRENCIES = (
        ("$" , "USD"),
        ("IQD" , "IQD")
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='items')
    name = models.CharField(max_length=50)
    currency = models.CharField(max_length=3,choices=CURRENCIES,null=True)
    value = models.DecimalField(decimal_places=2,max_digits=7,null=True,blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f'{self.name} - {self.value}'

class Revenue(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='revenues')
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    total = models.DecimalField(decimal_places=2,max_digits=7,null=True,blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.item.name} - {self.quantity} ({self.total})'

    def save(self, *args, **kwargs):
        self.total = self.item.value * self.quantity

        super().save(*args,**kwargs)




class Expense(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='expenses')