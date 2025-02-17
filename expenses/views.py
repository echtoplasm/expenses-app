from django.shortcuts import render
from .models import Expense
# Create your views here.

def expense_list(request):
    expenses = Expense.objects.all()
    total_expense = sum(exp.amount for exp in expenses)
    return render(request, 'expenses/expense_list.html', {'expenses': expenses, 'total_expense': total_expense})
