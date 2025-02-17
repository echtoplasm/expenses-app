from django.db import models

# Create your models here.
class Expense(models.Model):
    CATEGORY_CHOICES = [
        ('ONLINE_SERVICES', 'Online Services'),
        ('TRAVEL', 'Travel'),
        ('FOOD', 'Food'),
        ('RENT', 'Rent'),
        ('OTHER', 'Other'),
    ]

    name = models.CharField(max_length=200)
    category = models.CharField(max_length=200, choices=CATEGORY_CHOICES)
    amount = models.DecimalField(max_digits=100, decimal_places=2)
    date = models.DateField()

    def __str__(self):
        return f"{self.name} - {self.amount} - {self.date}"

    
