from os import link
from matplotlib import ticker
import pandas as pd
import os

'''
LOGIN
Username: mohammad.aminazadeh98@gmail.com
password: 1328Koyfin4650
'''

ticker_ids = []

txt_files_directory = 'D://selenium project/selenium/Stock Links/1-USA/TXT Files'
for file in os.listdir(txt_files_directory):
    with open (os.path.join(txt_files_directory, file)) as txt_file:
        temp_links = []
        temp_ticker_ids = []
        temp_links = txt_file.readlines()
        temp_line = temp_links[0]

        # remove [] from beginning and ending of row
        temp_line = temp_line[1:-1]

        # separete all links with ','
        temp_links = temp_line.split(',')
        
        # remove the last link relating to help
        temp_links.pop()

        # remove "" and ?i=g from beginning and ending of each link
        temp_links = [element[1:-1] for element in temp_links]

        # extract stock ids from links
        temp_ticker_ids = [element[-9:] for element in temp_links]
        
        # add stock ids to main stock ids list
        ticker_ids.extend(temp_ticker_ids)

ticker_ids = list(set(ticker_ids))

# export ticker ids to excel
pd_dict = {
    "ticker_ids": ticker_ids
}

tickers_final_df = pd.DataFrame(pd_dict)
tickers_final_df.to_excel('D://selenium project/selenium/Stock Links/1-USA/Ticker ids 2.xlsx', index=False, header=True)
