'''
this script gets the latest market capitals and performances from tradingview.com website
NOTE: for each country, web_page_url (in line 39) and currency split (in line 81) must be updated
NOTE: All XPATHs must be checked with inspect element and changed.
'''


# imports
from selenium import webdriver
from time import sleep
import pandas as pd
from collections import defaultdict
from selenium.webdriver.common.by import By
import winsound


'''
LOGIN
amina_tradingview
1328Tradingview4650


CORS handler extention
https://chrome.google.com/webstore/detail/allow-cors-access-control/lhobafahddgcelffkeicbaginigeejlf


SetupVPN extension
https://chrome.google.com/webstore/detail/setupvpn-lifetime-free-vp/oofgbpoabipfcfjapgnbbjjaenockbdp
O6CEW6EZUI
'''

def create_main_df_dict():
    '''creates final data frame containing all stocks' columns for exporting to Excel file'''
    tickers_full_data = defaultdict(dict)

    tickers_full_data['Ticker Symbol'] = all_tickers_list
    tickers_full_data['Market Capital'] = all_market_capitals_list
    tickers_full_data['Monthly Perf'] = all_monthly_perfs_list
    tickers_full_data['3-Months Perf'] = all_three_months_perfs_list
    tickers_full_data['6-Months Perf'] = all_six_months_perfs_list
    tickers_full_data['Yearly Perf'] = all_yearly_perfs_list
    tickers_full_data['5-Years Perf'] = all_five_years_perfs_list

    return tickers_full_data

# def resize(list1, n):
#     '''raises the size of given list to n elements by inserting "NA" to beggining of the list'''
#     temp = list1
#     n_append = 11 - len(temp)
#     while n_append > 0:
#         temp.insert(0, 'NA')
#         n_append -= 1
#     return temp

# main web page url
web_page_url = "https://www.tradingview.com/markets/stocks-usa/market-movers-all-stocks/"


# setting up chrome driver
chrome_driver_path = "D://selenium project/chromedriver_win32/chromedriver.exe"
driver = webdriver.Chrome(executable_path=chrome_driver_path)
driver.maximize_window()


# primary lists of values
all_tickers_list = []
all_market_capitals_list = []
all_monthly_perfs_list = []
all_three_months_perfs_list = []
all_six_months_perfs_list = []
all_yearly_perfs_list = []
all_five_years_perfs_list = []


# go to targeted web page
driver.get(web_page_url)

print("===========================Please Change Tab to Valuation===============================")
# wait to have time to open list to the bottom manually
sleep(600)
print('Sleep 1 Ended!')


# all ticker rows
rows = driver.find_elements(By.XPATH, "//tr[@class='row-EdyDtqqh listRow']")


counter = len(rows)
for row in rows:

    # get all ticker symbols
    try:
        # get ticker symbols
        ticker_symbol = row.find_element(By.XPATH, "./td[1]/span/a").text
        all_tickers_list.append(ticker_symbol)
    except Exception as e:
        all_tickers_list.append("NA")
        print("--------------------Error in Ticker Symbol Section---------------------")
        print(e)
        

    # get all ticker market cpas column from 'valuation' tab
    try:
        # change 'USD' to proper currency if needed.
        markcet_cap = row.find_element(By.XPATH, "./td[3]").text.split('USD')[0]
        all_market_capitals_list.append(markcet_cap)
    except Exception as e:
        all_market_capitals_list.append("NA")
        print("--------------------Error in Market Cap Section---------------------")
        print(e)   

    print(f"{counter} Rows Left!")
    counter -= 1


# manually change tab to Performance
print("===========================Please Change Tab to Performance===============================")

# make four bip sound to alert user to change the tab
winsound.Beep(700, 900)
sleep(0.25)
winsound.Beep(700, 900)
sleep(0.25)
winsound.Beep(700, 900)
sleep(0.25)
winsound.Beep(700, 900)

# wait to change tab and expand list to the bottom
sleep(60)
print('Sleep 2 Ended!')

# all ticker rows
rows = driver.find_elements(By.XPATH, "//tr[@class='row-EdyDtqqh listRow']")

counter = len(rows)

for row in rows:

    # get all ticker monthly performance column from 'performance' tab
    try:
        monthly_perf = row.find_element(By.XPATH, "./td[4]/span").text
        all_monthly_perfs_list.append(monthly_perf)
    except Exception as e:
        all_monthly_perfs_list.append("NA")
        print("--------------------Error in Monthly Perf Section---------------------")
        print(e)


    # get all ticker 3-months performance column from 'performance' tab
    try:
        three_month_perf = row.find_element(By.XPATH, "./td[5]/span").text
        all_three_months_perfs_list.append(three_month_perf)
    except Exception as e:
        all_three_months_perfs_list.append("NA")
        print("--------------------Error in Three Months Perf Section---------------------")
        print(e)


    # get all ticker 6-months performance column from 'performance' tab
    try:
        six_month_perf = row.find_element(By.XPATH, "./td[6]/span").text
        all_six_months_perfs_list.append(six_month_perf)
    except Exception as e:
        all_six_months_perfs_list.append("NA")
        print("--------------------Error in Six Months Perf Section---------------------")
        print(e)


    # get all ticker yearly performance column from 'performance' tab 
    try:
        yearly_perf = row.find_element(By.XPATH, "./td[8]/span").text
        all_yearly_perfs_list.append(yearly_perf)
    except Exception as e:
        all_yearly_perfs_list.append("NA")
        print("--------------------Error in Yearly Perf Section---------------------")
        print(e)


    # get all ticker 5-year performance column from 'performance' tab
    try:
        five_year_perf = row.find_element(By.XPATH, "./td[9]/span").text
        all_five_years_perfs_list.append(five_year_perf)
    except Exception as e:
        all_five_years_perfs_list.append("NA")
        print("--------------------Error in Five Years Perf Section---------------------")
        print(e)

    print(f"{counter} Rows Left!")
    counter -= 1

print(f"Ticker Symbols length: {len(all_tickers_list)}")
print(f"MC length length: {len(all_market_capitals_list)}")
print(f"Monthly length: {len(all_monthly_perfs_list)}")
print(f"3 Months length: {len(all_three_months_perfs_list)}")
print(f"6 Months length: {len(all_six_months_perfs_list)}")
print(f"1 Year length: {len(all_yearly_perfs_list)}")
print(f"5 Years length: {len(all_five_years_perfs_list)}")



# export data to excel
data_df = pd.DataFrame(create_main_df_dict())
data_df.to_excel('D://selenium project/selenium/Stocks Data/1-USA/Market Cap and Perf Update 2023-01-01.xlsx', index=False, header=True)
