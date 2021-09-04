from django.urls import path, include
from rest_framework.routers import DefaultRouter
from dds.views import TypeOfExpensesViewSet, ExpensesViewSet


router_typeofexpenses = DefaultRouter()
router_typeofexpenses.register('typeofexpenses', TypeOfExpensesViewSet)

router_expenses = DefaultRouter()
router_expenses.register('expenses', ExpensesViewSet)

urlpatterns = [
    path('', include(router_typeofexpenses.urls)),
    path('', include(router_expenses.urls)),
]