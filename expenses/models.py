from django.db import models
from django.urls import reverse
# Create your models here.

class Expense(models.Model):
    CATEGORIES = (
        ('Food', 'Food'),
        ('Groceries', 'Groceries'),
        ('Personal', 'Personal'),
   
        ('Other', 'Other'),
    )
    name = models.CharField(max_length=100)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateField(auto_now=True)
    category = models.CharField(max_length=100, choices=CATEGORIES)
    

    def __str__(self):
        return self.name
    
    class Meta:
        ordering = ['-date']
    
    def get_absolute_url(self):
        return reverse('expenses:detail', kwargs={'pk': self.id})