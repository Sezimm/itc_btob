from rest_framework.viewsets import ModelViewSet

from dds.models import TypeOfExpenses, Expenses
from dds.serializers import TypeOfExpensesSerializer, ExpensesSerializer



class TypeOfExpensesViewSet(ModelViewSet):
    queryset = TypeOfExpenses.objects.all()
    serializer_class = TypeOfExpensesSerializer
    ordering_fields = ['title', ]

    # def get_serializer_context(self):
    #     return {'request': self.request, 'action': self.action}


class ExpensesViewSet(ModelViewSet):
    queryset = Expenses.objects.all()
    serializer_class = ExpensesSerializer
    search_fields = ['type', ]
    ordering_fields = ['summa', ]
    filterset_fields = ['type',]
