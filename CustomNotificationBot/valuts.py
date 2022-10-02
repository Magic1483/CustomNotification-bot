import requests
import json
import codecs
import time
import telebot
# Import libraries
import json
import requests

# defining key/request url
#CRYPTO PRICE  PAGE
#https://www.geeksforgeeks.org/get-real-time-crypto-price-using-python-and-binance-api/



def get_price(crypto):
  try:
      crypto=crypto.upper()

      key = f"https://api.binance.com/api/v3/ticker/price?symbol={crypto}USDT"

      # requesting data from url


      data = requests.get(key)
      data = data.json()
      #str=f"{crypto}:{round(float(data['price']),3)} USDT"
      return float(data['price'])
  except:
    return 'not found'

    


#print(type(get_price('BTC')))