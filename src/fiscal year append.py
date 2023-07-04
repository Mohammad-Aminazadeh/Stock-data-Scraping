'''
this script appends last fiscal year data scraped from Koyfin to the main dataset
'''

# imports
import pandas as pd
from collections import defaultdict



# open excel file
df1 = pd.read_excel("D://selenium project/selenium/Stocks Data/1-USA/Tickers Full Data.xlsx")
df2 = pd.read_excel("D://selenium project/selenium/Stocks Data/1-USA/Fiscal Year 2022 Update/Tickers Full Data.xlsx")

# from scraped ids, append the ones that does not exist in excel file into scraped ids2 
df3 = pd.merge(df1, df2, on='Ticker Symbol', how='outer')

# export new df to excel
df3.to_excel("D://selenium project/selenium/Stocks Data/1-USA/Fiscal Year 2022 Update/Full Data FY2022 Update.xlsx", index=False, header=True)