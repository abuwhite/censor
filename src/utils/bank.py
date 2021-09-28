"""Account module."""


class BankAccount(object):
    def __init__(self,
                 _income=0,
                 _expenses=0,
                 _percent=10
                 ):
        """

        :param _income: Доход
        :param _expenses: Расход
        :param _percent: Процент
        """
        self._income = _income
        self._expenses = _expenses
        self._percent = _percent
        self._balance = 0

    @property
    def income(self):
        """Получить сумму дохода."""
        return int(self._income)

    @property
    def expenses(self):
        """Получить сумму расходов."""
        return int(self._expenses)

    @property
    def percent(self):
        """Получить процент."""
        return self._percent

    @property
    def capital(self):
        """Получить сумму накоплений по формуле

        ((Доход - Расход) / 100) * Процент

        """
        return int(((self._income - self._expenses) / 100) * self._percent)

    @property
    def balance(self):
        """Получить свободную сумму после всех вычетов."""
        self._balance = self._income - self._expenses - self.capital
        return self._balance

    @property
    def balance_for_day(self):
        """Получить сумму свободных денег на день."""
        return self._balance / 31

    @property
    def capital_year(self):
        """Получить сумму накоплений за 12 месяцев."""
        return self.capital * 12
