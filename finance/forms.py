from django import forms
from django.http import HttpRequest

from .models import CreditAccount, DebitAccount


class OpenAccountForm(forms.Form):
    ACCOUNT_CHOICES = [
        ('-', '---Choose account type---'),
        ('debit', 'Debit Account'),
        ('credit', 'Credit Account'),
    ]
    #initial
    account_type = forms.ChoiceField(choices=ACCOUNT_CHOICES, required=True, initial='-')

    #common
    initial_funds = forms.DecimalField(max_digits=10, decimal_places=2, initial=0)

    #debit
    default_commission = forms.DecimalField(max_digits=4, decimal_places=2, 
                                            initial=DebitAccount._meta.get_field('default_commission').default)
    cashback_rate = forms.DecimalField(max_digits=4, decimal_places=2, 
                                       initial=DebitAccount._meta.get_field('cashback_rate').default)

    #credit
    credit_limit = forms.DecimalField(max_digits=10, decimal_places=2, initial=1000.0)

    def __init__(self, *args, **kwargs):
        self.request: HttpRequest = kwargs.pop('request', None)# we use pop 'cause BaseForm doesn't have this argument
        super().__init__(*args, **kwargs)

    def clean_account_type(self):
        account_type = self.cleaned_data.get('account_type')
        if account_type == '-':
            raise forms.ValidationError("Please choose account type")

        return account_type
    
    def save(self):
        account_type = self.cleaned_data.get("account_type")
        initial_funds = self.cleaned_data.get("initial_funds")
        user = self.request.user

        if account_type == "credit":
            credit_limit = self.cleaned_data.get("credit_limit")
            return CreditAccount.objects.create(
                                        user=user,
                                        funds=initial_funds,
                                        credit_limit=credit_limit,
                                        current_credit=0)
        elif account_type == "debit":
            default_commission = self.cleaned_data.get("default_commission")
            cashback_rate = self.cleaned_data.get("cashback_rate")
            return DebitAccount.objects.create(
                                        user=user,
                                        funds=initial_funds,
                                        default_commission=default_commission,
                                        cashback_rate=cashback_rate)
