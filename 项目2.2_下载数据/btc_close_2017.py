from __future__ import (absolute_import, division, print_function, unicode_literals)
try:
    from urllib import urlopen
except ImportError:
    from urllib.request import urlopen
import json

json_file = 'btc_close_2017.json'
with open(json_file) as file:
    btc_data = json.load(file)

for btc_dict in btc_data:
    date = btc_data['date']
    month = btc_data['month']
    week = btc_data['week']
    weekday = btc_data['weekday']
    close = btc_data['close']
    

