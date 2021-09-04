from django.db import models


class TypeOfExpenses(models.Model):
    title = models.CharField(max_length=250)

    def __str__(self):
        self.title


class Expenses(models.Model):
    type = models.ForeignKey(TypeOfExpenses, on_delete=models.CASCADE)
    summa = models.DecimalField(max_digits=10, decimal_places=2)
    date_of_add = models.DateField(auto_now=False)
    comment = models.TextField(null=True, blank=True)

    
