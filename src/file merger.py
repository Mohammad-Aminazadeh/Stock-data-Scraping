# imports
import pandas as pd

# read files that needs to be merged
df1 = pd.read_excel("D://selenium project/selenium/Stocks Data/1-USA/Tickers Full Data.xlsx")
df2 = pd.read_excel("D://selenium project/selenium/Stocks Data/1-USA/Market Cap and Perf Update 2023-02-05.xlsx")

# merge two files on Ticker Symbol column
df3 = pd.merge(df1, df2, on='Ticker Symbol', how='left')


# export new data frame to excel
df3.to_excel("D://selenium project/selenium/Stocks Data/1-USA/Updated Full Data 2023-02-05.xlsx", index=False, header=True)
