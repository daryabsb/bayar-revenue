from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Revenue(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='revenues')
    item = models.CharField(max_length=200)
    value = models.DecimalField(decimal_places=2,max_digits=7)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
