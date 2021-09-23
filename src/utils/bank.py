"""Модуль Банка."""


class Bank(object):
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
        """Получить сумму свободных средств по формуле

        ((Доход - Расход) / 100) * Процент

        """
        return int(((self._income - self._expenses) / 100) * self._percent)

    @property
    def free(self):
        """Получить свободную сумму после всех вычетов."""
        return self._income - self._expenses - self.capital

    @property
    def capital_year(self):
        """Получить сумму накоплений за 6 месяцев."""
        return self.capital * 6
