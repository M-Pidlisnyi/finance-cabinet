from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from django.views.generic import DetailView

from .models import FinanceAccount, CreditAccount, DebitAccount

# Create your views here.
def index(request:HttpRequest):
    current_user = request.user
    context = {}
    if current_user.is_authenticated:
        user_accounts = FinanceAccount.objects.filter(user=current_user)

        total_acc_number = len(user_accounts)
        #if not planning to iterate over them don't use len() for querysets, insteas use .count()
        #in this case we WILL iterate so len() MIGHT be faster

        context = {"accounts": user_accounts,  "acc_num": total_acc_number}


    return render(request, 'finance/index.html', context=context)


class FinAccountDetailView(DetailView):
    model = FinanceAccount
    template_name = 'finance/account_detail.html'


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        account_type = type(self.get_object()).__name__
        context['account_type'] = account_type

        return context


