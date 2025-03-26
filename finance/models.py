from datetime import datetime
from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator


# Create your models here.
class Category(models.Model):
    """model that represents the category of payment or saving goal"""
    name = models.CharField(max_length=25)

    class Meta:
        verbose_name_plural = 'Categories'

class FinanceAccount(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='accounts')
    funds = models.DecimalField(verbose_name="user's own funds", decimal_places=2, max_digits=10)
   

class DebitAccount(FinanceAccount):
    default_commission = models.DecimalField(decimal_places=2, max_digits=4, default=0.35,
                                             validators=[MinValueValidator(0.01)],
                                             verbose_name="default commission (%)",help_text="base(but not only) commission for each transaction")
    cashback_rate= models.DecimalField(decimal_places=2, max_digits=4, default=1.35,
                                       verbose_name="default cashback (%)", help_text="this cashback will be received from some categories of transaction")
    accumulated_cashback = models.DecimalField(decimal_places=2, max_digits=10, default=0)

class CreditAccount(FinanceAccount):
    credit_limit = models.DecimalField(decimal_places=2, max_digits=10)
    current_credit = models.DecimalField(decimal_places=2, max_digits=10)

class SavingsGoal(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    interest_rate = models.DecimalField(decimal_places=2, default=0.0, max_digits=4)
    goal_sum = models.DecimalField(decimal_places=2, max_digits=10)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True)
    deadline = models.DateField(null=True, blank=True)

class Deposit(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    principal = models.DecimalField(decimal_places=2, max_digits=10)
    interest_rate = models.DecimalField(decimal_places=2, max_digits=4, verbose_name="interest rate (%)")
    period = models.IntegerField()
    payments_per_year = models.IntegerField()
    start_date = models.DateField()

class Transaction(models.Model):
    datetime = models.DateTimeField(default=datetime.now)
    amount = models.DecimalField(decimal_places=2, max_digits=10)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True)    
    is_successful = models.BooleanField(default=True)
    from_account = models.ForeignKey(FinanceAccount, on_delete=models.CASCADE, related_name='payments_from')
    to_account = models.ForeignKey(FinanceAccount, on_delete=models.CASCADE, related_name='payments_to')
