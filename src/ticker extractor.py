'''
this script extracts all ticker symbols from a text file (from tradingview.com) and stores in an excel file
'''


# imports
from h11 import Data
import pandas as pd

all_tickers = []
with open("D://selenium project/selenium/Stock Links/5-China/All Tickers.txt") as ticker_links_file:
    ticker_links = ticker_links_file.readlines()
    # print(ticker_links)

    # removing [] from start and end of file
    ticker_links = ticker_links[0][1:-1]

    # separete all links with ','
    ticker_links = ticker_links.split(',')

    # remove "" from each link
    ticker_links = [line[1:-1] for line in ticker_links]

    for ticker_link in ticker_links:
        if 'https://www.tradingview.com/symbols/' in ticker_link:
            
            # extracting ticker symbol from link
            temp_link = ticker_link.split('symbols')[1][1:-1].split('-')[1]
            all_tickers.append(temp_link)

# writing tickers to excel file
tickers_dict = {}
tickers_dict['Ticker'] = all_tickers
tickers_df = pd.DataFrame(tickers_dict)
tickers_df.to_excel('D://selenium project/selenium/Stock Links/5-China/All Tickers.xlsx', header=True, index=False)
