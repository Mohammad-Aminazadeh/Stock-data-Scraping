'''
this script gets the latest market capitals and performances from tradingview.com website
NOTE: for each country, web_page_url (in line 39) and currency split (in line 81) must be updated
NOTE: All XPATHs must be checked with inspect element and changed.
'''


# imports
import pandas as pd
from collections import defaultdict

do_not_scrape_df = pd.read_excel("D://selenium project/selenium/Stocks Data/1-USA/Fiscal Year 2022 Update/Not Scrape.xlsx")
do_not_scrape_tickers = list(do_not_scrape_df['Ticker'])

do_scrape_tickers = []
do_scrape_ids = []
# print(do_not_scrape_tickers)

with open("D://selenium project/selenium/Stocks Data/1-USA/Fiscal Year 2022 Update/scraped ids.txt", 'r') as scraped_file:
    scraped_lines = [line.rstrip() for line in scraped_file.readlines()]
    # print(len(scraped_lines))
    # scraped_tickers = [scraped_object.split(':')[0] for scraped_object in scraped_lines]
    # scraped_ids = [scraped_object.split(':')[1] for scraped_object in scraped_lines]

    for i in range(len(scraped_lines)):
        ticker = scraped_lines[i].split(':')[0]
        id = scraped_lines[i].split(':')[1]

        if ticker not in do_not_scrape_tickers:
            do_scrape_tickers.append(ticker)
            do_scrape_ids.append(id)

main_df_dict = dict()
main_df_dict['Ticker'] = do_scrape_tickers
main_df_dict['ID'] = do_scrape_ids

main_df = pd.DataFrame(main_df_dict)
main_df.to_excel("D://selenium project/selenium/Stock Links/1-USA/Tickers with IDs.xlsx", index=False, header=True)

# print(len(do_scrape_tickers))



# export data to excel
# data_df.to_excel('D://selenium project/selenium/Stocks Data/1-USA/Market Cap and Perf Update 2023-02-05.xlsx', index=False, header=True)
