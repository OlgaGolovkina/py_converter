from flask import Flask, request, json
import urllib.request
import ssl


app = Flask(__name__)

ssl._create_default_https_context = ssl._create_unverified_context

CURRENCY_LIST = ("USD", "EUR", "JPY")


@app.route('/', methods=['POST', 'GET'])
def index():
    from_currency = request.args.get('from')
    to_currency = request.args.get('to')
    amount = request.args.get('amount')
    if not (from_currency and to_currency and amount):
        return "Missing parameters", 400
    try:
        amount = float(amount)
    except ValueError:
        return "Invalid parameters", 400
    if from_currency not in CURRENCY_LIST or to_currency not in CURRENCY_LIST:
        return "Invalid parameters", 400
    req = urllib.request.Request('https://api.exchangeratesapi.io/latest')
    response = urllib.request.urlopen(req)
    page = response.read()

    j = json.loads(page.decode("utf-8"))
    USD_EUR = j["rates"]["USD"]
    JPY_EUR = j["rates"]["JPY"]

    result = amount
    if from_currency == "USD":
        result /= USD_EUR
    elif from_currency == "JPY":
        result /= JPY_EUR

    if to_currency == "USD":
        result *= USD_EUR
    elif to_currency == "JPY":
        result *= JPY_EUR

    return str(round(result, 2)), 200


if __name__ == '__main__':
    app.debug = True
    app.run()
