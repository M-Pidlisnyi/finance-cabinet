from datetime import datetime
from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Category(models.Model):
    """model that represents the category of payment or saving goal"""
    name = models.CharField(max_length=25)

    class Meta:
        verbose_name_plural = 'Categories'

class DebitAcccount(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='accounts')
    funds = models.DecimalField(verbose_name="own user's funds", decimal_places=2, max_digits=10)
    

class CreditAccount(DebitAcccount):
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
    interest_rate = models.DecimalField(decimal_places=2, max_digits=4)
    period = models.IntegerField()
    payments_per_year = models.IntegerField()
    start_date = models.DateField()

class Transaction(models.Model):
    datetime = models.DateTimeField(default=datetime.now)
    amount = models.DecimalField(decimal_places=2, max_digits=10)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True)    
    is_successful = models.BooleanField(default=True)
    from_account = models.ForeignKey(DebitAcccount, on_delete=models.CASCADE, related_name='payments_from')
    to_account = models.ForeignKey(DebitAcccount, on_delete=models.CASCADE, related_name='payments_to')
