import requests
import math
import random
import re
from Score import add_score


def get_money_interval(difficulty):
    usd_amount = random.randint(1, 100)
    req = requests.get('https://v6.exchangerate-api.com/v6/615ee5a543815d1e4d0f04da/latest/USD')
    res = req.json()
    convert_rates = res['conversion_rates']
    currency = round(convert_rates['ILS'], 2)
    interval = (currency * usd_amount - (5 - difficulty), currency * usd_amount + (5 - difficulty))
    print(f'How much ILS (must be with agorot included) you will get from ${usd_amount} '
          f'if the currency rate is {currency}?')
    return interval


def get_guess_from_user(interval, difficulty):
    while True:
        user_guess = input(f'What is your guess:')
        if not re.match("^[a-zA-Z0-9]*$", user_guess):
            break
    if math.trunc(interval[0]) <= float(user_guess) <= math.trunc(interval[1]):
        add_score(difficulty)
        return True
    else:
        return False


def play(difficulty):
    return get_guess_from_user(get_money_interval(difficulty), difficulty)
