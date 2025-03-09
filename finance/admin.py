from django.contrib import admin
from .models import Category, DebitAcccount, CreditAccount, SavingsGoal, Deposit, Transaction
# Register your models here.

admin.site.register(Category)
admin.site.register(DebitAcccount)
admin.site.register(CreditAccount)
admin.site.register(SavingsGoal)
admin.site.register(Deposit)
admin.site.register(Transaction)