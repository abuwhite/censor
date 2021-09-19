from flask import Flask, render_template, request
import locale

app = Flask(__name__)

locale.setlocale(locale.LC_ALL, "kk_KZ")


user = 'Какое-то имя'
MONEY = 0
AMOUNT = 0

# formatted = locale.currency(MONEY)


class Formatted(object):
    def __init__(self, value=0):
        self.money = value

    def money(self):
        return self.money

    def currency(self):
        return locale.currency(self.money)

    def add_money(self, value):
        if isinstance(value, int):
            self.money = value
        else:
            print('Error')

formatted = Formatted()


@app.route('/')
def index():
    return render_template('index.html', name=user, amount=formatted.currency())


@app.route('/', methods=['POST'])
def my_form_post():
    pass
    # print(request.form)
    # print(request.form['amount'])
    # print(request.form['loan'])

    # if request.form['amount'] == '':
    #     formatted.add_money(0)
    # else:
    #     formatted.add_money(int(request.form['text']))

    # return render_template('index.html', name=user, amount=formatted.currency(), value=formatted.money)


if __name__ == '__main__':
    app.run(host='0.0.0.0')
