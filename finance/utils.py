
from .models import FinanceAccount, CreditAccount, DebitAccount


def get_account_type(account: FinanceAccount) -> tuple[str, CreditAccount|DebitAccount]:
    """Determine the type of account (Credit or Debit) and return the string with the type name
    and specific account object."""

    if hasattr(account, "creditaccount"):
        return "Credit", account.creditaccount
    elif hasattr(account, "debitaccount"):
        return "Debit", account.debitaccount
    else:
        return "Unkonwn", account