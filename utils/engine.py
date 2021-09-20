class Formatted(object):
    def __init__(self, value=0):
        self.money = value

    def money(self):
        return self.money

    def capital(self):

        # self.money = (self.money / 100) * 60
        self.capital = (self.money / 100) * 60
        return self.capital

    def currency(self):
        return locale.currency(self.money)

    def add(self, value):
        self.money = value
        if isinstance(value, int):
            self.money = value

    def remove(self, value):
        if isinstance(value, int):
            self.money -= value