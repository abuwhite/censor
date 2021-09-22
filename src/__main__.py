from flask import (
    Flask,
    render_template,
    request,
    redirect
)

from src.utils import engine

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html', amount=200000)


@app.route('/info')
def test():
    return render_template('info.html')


@app.route('/', methods=['POST'])
def my_form_post():
    # print('[AMOUNT FORM]', request.form['amount'], type(request.form['amount']))
    # print('[LOAN FORM]', request.form['loan'], type(request.form['loan']))
    # print('[CAPITAL FORM]', request.form['capital'], type(request.form['capital']))
    amount = int(request.form['amount'])
    loan = int(request.form['loan'])
    capital = int(request.form['capital'])

    bank = engine.Bank(
        _amount=amount,
        _loan=loan,
        _capital=capital
    )

    print('[AMOUNT]', bank.amount)
    print('[LOAN]', bank.loan)
    print('[CAPITAL]', bank.capital)

    # bank.capital = 90
    #
    # print('[NEW CAPITAL]', bank.capital)


    # if request.form['amount'] == '':
    #     bank.add(0)
    # else:
    #     bank.add(int(request.form['amount']))
    #
    # if request.form['loan'] == '':
    #     bank.remove(0)
    # else:
    #     bank.remove(int(request.form['loan']))


    return redirect('/')


if __name__ == '__main__':
    app.run(host='0.0.0.0')
