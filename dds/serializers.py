from rest_framework import serializers
from .models import *


class TypeOfExpensesSerializer(serializers.ModelSerializer):
    class Meta:
        model = TypeOfExpenses
        fields = ('title', )


class ExpensesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Expenses
        fields = ('type', 'summa', 'date_of_add', 'comment',)



