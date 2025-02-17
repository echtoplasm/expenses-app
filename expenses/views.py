from django.shortcuts import render, redirect
from .models import Expense
from .forms import ExpenseForm
# Create your views here.

def expense_list(request):
    expenses = Expense.objects.all()
    total_expense = sum(exp.amount for exp in expenses)


    if request.method == 'POST':
        form = ExpenseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('expense_list')
    else:
        form = ExpenseForm()

    return render(request, 'expenses/expense_list.html', {
        'expenses': expenses,
        'total_expense': total_expense,
        'form': form
    })

