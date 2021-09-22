import locale

locale.setlocale(locale.LC_ALL, "kk_KZ")


class Bank(object):
    def __init__(self,
                 _amount=0,
                 _loan=0,
                 _capital=60
                 ):
        self._amount = _amount
        self._loan = _loan
        self._capital = _capital

    @property
    def amount(self):
        return self._amount

    @amount.setter
    def amount(self, new):
        self._amount = new

    @property
    def loan(self):
        return self._loan

    @loan.setter
    def loan(self, new):
        self._loan = new

    @property
    def capital(self):
        return ((self._amount - self._loan) / 100) * self._capital

    @capital.setter
    def capital(self, value):
        self._capital = value

    #
    # def currency(self):
    #     return locale.currency(self.money)