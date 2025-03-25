from django import forms

class OpenAccountForm(forms.Form):
    ACCOUNT_CHOICES = [
        ('-', '---Choose account type---'),
        ('debit', 'Debit Account'),
        ('credit', 'Credit Account'),
    ]
    #initial
    account_type = forms.ChoiceField(choices=ACCOUNT_CHOICES, required=True, initial='-')

    #common
    initial_funds = forms.DecimalField(max_digits=10, decimal_places=2, initial=0, disabled=True)

    #debit
    default_commission = forms.DecimalField(max_digits=4, decimal_places=2, initial=0.0, disabled=True)
    cashback_rate = forms.DecimalField(max_digits=4, decimal_places=2, initial=0.0, disabled=True)

    #credit
    credit_limit = forms.DecimalField(max_digits=10, decimal_places=2, initial=0, disabled=True)

    def clean_account_type(self):
        account_type = self.cleaned_data.get('account_type')
        if account_type == '-':
            raise forms.ValidationError("Please choose account type")

        return account_type
    
    def save(self):
        ...