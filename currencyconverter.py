##for currency converter would need a database to feed real time currency values
##get those real time currency values stored in a database under different variable names
##create a function that will retrieve one currency - divide by the other then output the float value
##create a seperate function that would do the inverse if they want y represented as x

##install packages pandas
##install packages 'requests-html' to parse through the web data requests

import requests
##retrival of exchange rates from third party API
def get_exchange_rates():
    api_url = "https://api.exchangerate-api.com/v4/latest/USD"
    response = requests.get(api_url)
    data = response.json()
    return data["rates"]
exchange_rates = get_exchange_rates()

##define function of currency conversion
def currency_conversion():
    ## get the intial amount of money that is going to be converted
    money= input(int("How much do you want to convert"))
    ## check what their base currency is
    basecurrency = input("What is your base currency")
    ## check what they want to convert to to be able to retrieve the exchange rate between the two currencies
    desiredcurrency = input("What is your desired currency")
    ##check there is an exchange rate for the two currencies
    if basecurrency and desiredcurrency in exchange_rates:
        ##the value of money you would get in the exchanged currency
           exchangedcurrency = money * (basecurrency*exchange_rates)
    return exchangedcurrency
##i forgot how to use functions
currency_conversion()

