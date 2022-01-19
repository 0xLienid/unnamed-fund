import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from pycoingecko import CoinGeckoAPI

def getTokenList():
  cg = CoinGeckoAPI()
  tokenList = [token['symbol'] for token in cg.get_coins_list()]
  return tokenList

def setTweetParams(symbol, numTweets):
  baseUrl = 'https://twitter.com/search?q='
  tweetParams = {'symbol': symbol, 'url': baseUrl + symbol, 'numTweets': str(numTweets)}

if __name__ == "__main__":
  print(getTokenList())