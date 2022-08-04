import requests
import json
from pathlib import Path
import re, csv



# create a function for exchange rate
def exchange_rate():
    # set variable url to 
    url = 'https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE&from_currency=USD&to_currency=SGD&apikey=SWG3LWP6GD58C1QL'
    # request to get api from alphavantage
    r = requests.get(url)
    # retrieve data with .json from response and save it as data
    data = r.json()
    # create an empty list
    currency_list = []
    # append the empty list with the currency exchange rate
    currency_list.append(data["Realtime Currency Exchange Rate"]["5. Exchange Rate"])
    # extract exchange rate from the list and convert into float
    currency = float(currency_list[0])

    # create a path to the summary_report.txt file
    current = Path.cwd()/"summary_report.txt"
    # create a summary_report with .touch()
    current.touch()

    # open the summary_report.txt in append mode
    with current.open(mode="a", encoding = "UTF-8", newline = "") as file:
        # round up the currency to 5 decimal places
        exchange_round = round(currency,5)
        msg = "[REAL TIME CURRENCY CONVERSION RATE] US$1 = SGD" + str(exchange_round) +'\n'
        # write the realtime currency exchange rate and append into summary_report.txt file
        file.write(msg)  
    # return the currency exchange rate 
    return currency
