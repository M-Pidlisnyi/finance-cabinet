
from .models import FinanceAccount, CreditAccount, DebitAccount


def get_account_type(account: FinanceAccount) -> tuple[str, CreditAccount|DebitAccount]:
    """
    WARDNINIG: this is a legacy function, written before polymorphic models were used.
    Determine the type of account (Credit or Debit) and return the string with the type name
    and specific account object."""

    if isinstance(account, CreditAccount):
        return "Credit", account
    elif isinstance(account, DebitAccount):
        return "Debit", account
    else:
        raise ValueError("Unknown account type")