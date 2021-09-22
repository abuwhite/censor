from flask import (
    Flask,
    render_template,
    request,
    redirect
)

from src.utils.bank import Bank, get_month_amount
from babel import numbers

app = Flask(__name__)

user = Bank()


def currency(num):
    return numbers.format_currency(num, 'KZT', locale='kk_KZ')


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/', methods=['POST'])
def my_form_post():
    global user
    user = Bank(_amount=int(request.form['amount']),
                _loan=int(request.form['loan']),
                _percent=int(request.form['capital'])
                )

    return redirect('/info')


@app.route('/info')
def test():
    print(user.percent)
    return render_template('info.html',
                           percent=user.percent,
                           month=currency(get_month_amount(user.capital)),
                           loan=currency(user.loan),
                           capital=currency(user.capital),
                           amount=currency(user.free)
                           )


if __name__ == '__main__':
    app.run(host='0.0.0.0')
