"""
Exercise 5 — Composition and factory methods

Tasks:
- Implement Account and Transaction classes. Account composes a list of Transaction objects.
- Implement Account.deposit(amount), Account.withdraw(amount) and a @classmethod from_dict(cls, data) factory that constructs an Account from a dict.
- Transactions should be immutable records with amount and description.

Run tests: python src/ex5_composition_factory.py
"""
import unittest
from typing import List

class Transaction:
    """Immutable transaction record.

    Attributes:
        amount (float): positive for deposit, negative for withdrawal
        description (str): text description
    """
    def __init__(self, amount: float, description: str):
        """Create a Transaction. amount may be positive or negative. description cannot be empty."""
        raise NotImplemented


class Account:
    """Bank account that composes transactions.

    Behavior:
        - balance is the sum of all transaction amounts
        - deposit and withdraw create Transaction objects and add them to the account
    """

    def __init__(self, owner: str, transactions: List[Transaction] = None):
        """Create an Account. Owner must be non-empty."""
        raise NotImplemented

    @property
    def balance(self) -> float:
        """Return the current balance as sum of transaction amounts."""
        raise NotImplemented

    def deposit(self, amount: float, description: str = 'deposit') -> None:
        """Add a deposit transaction.

        Raises:
            ValueError: if amount is not positive or description empty
        """
        raise NotImplemented

    def withdraw(self, amount: float, description: str = 'withdraw') -> None:
        """Add a withdrawal transaction (as negative amount).

        Raises:
            ValueError: if amount is not positive or description empty
        """
        raise NotImplemented

    @classmethod
    def from_dict(cls, data: dict):
        """Factory to create Account from a dict with keys: owner (str), transactions (list of dicts).

        Each transaction dict has keys 'amount' and 'description'.
        """
        raise NotImplemented


# -------------------- Tests --------------------
class TestAccountComposition(unittest.TestCase):
    def test_transaction_and_account_basic(self):
        t = Transaction(100, 'initial')
        a = Account('Bob', [t])
        self.assertEqual(a.owner, 'Bob')
        self.assertEqual(a.balance, 100)

    def test_deposit_withdraw(self):
        a = Account('Sally')
        a.deposit(50, 'pay')
        self.assertEqual(a.balance, 50)
        a.withdraw(20, 'atm')
        self.assertEqual(a.balance, 30)

    def test_invalid_ops(self):
        with self.assertRaises(ValueError):
            Transaction(10, '')
        a = Account('Z')
        with self.assertRaises(ValueError):
            a.deposit(0, 'x')
        with self.assertRaises(ValueError):
            a.withdraw(-1, 'x')

    def test_factory(self):
        data = {
            'owner': 'Factory',
            'transactions': [
                {'amount': 100, 'description': 'start'},
                {'amount': -30, 'description': 'buy'}
            ]
        }
        a = Account.from_dict(data)
        self.assertEqual(a.owner, 'Factory')
        self.assertEqual(a.balance, 70)


if __name__ == '__main__':
    unittest.main()
