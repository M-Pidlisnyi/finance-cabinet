from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpRequest, HttpResponse
from django.views.generic import DetailView, CreateView

from .models import FinanceAccount, CreditAccount, DebitAccount
from .forms import OpenAccountForm
from .utils import get_account_type

# Create your views here.
def index(request:HttpRequest):
    current_user = request.user
    context = {}
    if current_user.is_authenticated:
        user_accounts = FinanceAccount.objects.filter(user=current_user)

        #if not planning to iterate over them don't use len() for querysets, insteas use .count()
        #in this case we WILL iterate so len() MIGHT be faster
        total_acc_number = len(user_accounts)

        accounts_with_type = [get_account_type(account) for account in user_accounts]

        context = {"accounts": accounts_with_type,  "acc_num": total_acc_number}


    return render(request, 'finance/index.html', context=context)


class FinAccountDetailView(DetailView):
    model = FinanceAccount
    template_name = 'finance/account_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        account_type, account = get_account_type(self.get_object())
        
        context["account"] = account
        context["account_type"] = account_type

        return context


def open_account(request:HttpRequest):
    if request.method == 'POST':
        form = OpenAccountForm(request.POST, request=request)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = OpenAccountForm()
    return render(request, 'finance/open_account.html', {'form': form})


def close_account(request:HttpRequest, pk:int):
    acc_to_delete = get_object_or_404(FinanceAccount, pk=pk)
    funds = acc_to_delete.funds

    debt = acc_to_delete.current_credit if isinstance(acc_to_delete, CreditAccount) else 0
    accumulated_cashback = acc_to_delete.accumulated_cashback if isinstance(acc_to_delete, DebitAccount) else 0

    if request.method == 'POST':
        confimred = request.POST.get('confirm', False)
        if confimred:
            print("Deleting account...")
            return redirect('finacc-close', pk=pk)
        else:
            return redirect('finacc-close', pk=pk)

    context = {
        "account": acc_to_delete,
        "funds": funds, 
        "debt": debt,
        "accumulated_cashback": accumulated_cashback,

    }

    return render(request, "finance/close_account.html", context=context)