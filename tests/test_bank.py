"""Bank class testing."""

from app.main.bank import BankAccount

account = BankAccount()


def test_create_account():
    """Test new account."""
    actual = BankAccount()
    assert actual._income == 0
    assert actual._expenses == 0
    assert actual._percent == 10
    assert actual._balance == 0


def test_bank_account():
    """Test capital, balance and expenses."""
    actual = BankAccount(_income=200000, _expenses=25000, _percent=60)

    assert actual.income == 200000
    assert actual.capital == 105000
    assert actual.balance == 70000
    assert actual.expenses == 25000
    assert actual.percent == 60
    assert actual.balance_for_day == 2258.064516129032
    assert actual.capital_year == 1260000
