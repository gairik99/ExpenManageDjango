from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Expense(models.Model):
    user_name = models.ForeignKey(User, on_delete=models.CASCADE,related_name='expenses')
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.CharField(max_length=255)
    date = models.DateField()

    def __str__(self):
        return f"{self.user_name} - {self.amount} - {self.description} - {self.date}"