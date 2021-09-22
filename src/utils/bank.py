class Bank(object):
    def __init__(self,
                 _amount=0,
                 _loan=0,
                 _percent=10
                 ):
        self._amount = _amount
        self._loan = _loan
        self._percent = _percent

    @property
    def amount(self):
        return int(self._amount)

    @amount.setter
    def amount(self, new):
        self._amount = new

    @property
    def loan(self):
        return int(self._loan)

    @loan.setter
    def loan(self, new):
        self._loan = new

    @property
    def percent(self):
        return self._percent

    @property
    def capital(self):
        return int(((self._amount - self._loan) / 100) * self._percent)

    @property
    def free(self):
        return self._amount - self._loan - self.capital


def get_month_amount(num):
    return num * 12
