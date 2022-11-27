# main.py
from scrapePackage.Scrape import *

def demo():
    '''
    Test our functions
    '''
    price = get_stock_price("GOOGL")
    print("Price", price)

    market_cap = get_stock_current_market_cap("GOOGL")
    print("Market Cap", market_cap)
    
    
def buildPortfolio():
    # Build a Portfolio and scrape that
    myPortfolio = {"Google":"GOOGL", "Coke":"KO","Procter and Gamble":"PG","Home Depot":"HD"}
#    for i in range(0,100000000):
    for key in myPortfolio:
        print(myPortfolio[key] + "...")
        price = get_stock_price(myPortfolio[key])
        print(key + ":" + price)
demo()