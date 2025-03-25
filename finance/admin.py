from django.contrib import admin
from .models import Category, DebitAccount, CreditAccount, SavingsGoal, Deposit, Transaction
# Register your models here.

admin.site.register(Category)
admin.site.register(DebitAccount)
admin.site.register(CreditAccount)
admin.site.register(SavingsGoal)
admin.site.register(Deposit)
admin.site.register(Transaction)