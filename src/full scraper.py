'''
this is tha primary script that scrapes all the values of tickers from app.koyfin.com
'''

# imports
from asyncio.log import logger
from distutils.command.build_scripts import first_line_re
from time import time
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from time import sleep
import pandas as pd
from collections import defaultdict
from selenium.webdriver.common.by import By

'''
LOGIN
mohammad.aminazadeh98@gmail.com
1328Koyfin4650


CORS handler extention
https://chrome.google.com/webstore/detail/allow-cors-access-control/lhobafahddgcelffkeicbaginigeejlf


FreeVPN extention
https://chrome.google.com/webstore/detail/free-vpn-for-chrome-vpn-p/majdfhpaihoncoakbjgbdhglocklcgno?hl=en


SetupVPN extension
https://chrome.google.com/webstore/detail/setupvpn-lifetime-free-vp/oofgbpoabipfcfjapgnbbjjaenockbdp
O6CEW6EZUI
'''

def resize(list1):
    '''raises the size of given list to 11 elements by inserting "NA" to beggining of the list'''
    temp = list1
    n_append = 11 - len(temp)
    while n_append > 0:
        temp.insert(0, 'NA')
        n_append -= 1
    return temp

def get_scraped_ids():
    '''returns a list of previously scraped ids'''
    scraped_list = []
    with open('D://selenium project/selenium/Stocks Data/9-India/Fiscal Year 2022 Update/scraped ids.txt') as scraped_file:
        scraped_list = scraped_file.readlines()
        scraped_list = [id.split(':')[1] for id in scraped_list]
        scraped_list = [id[:-1] for id in scraped_list]
    return scraped_list

def set_scraped_ids(scraped_list):
    '''writes the list of new scraped ids into scraped id text file'''
    with open('D://selenium project/selenium/Stocks Data/9-India/Fiscal Year 2022 Update/scraped ids.txt', mode='a') as scraped_file:
        for id in scraped_list:
            scraped_file.write(id + '\n')

def create_main_df_dict():
    '''creates final data frame containing all stocks' columns for exporting to Excel file'''
    tickers_full_data = defaultdict(dict)

    tickers_full_data['Ticker Symbol'] = all_ticker_symbols
    tickers_full_data['Company Name'] = all_company_names
    tickers_full_data['Industry'] = all_industries
    tickers_full_data['Sector'] = all_sectors
    tickers_full_data['Currency'] = all_currencies
    tickers_full_data['Market Capital'] = all_market_capitals
    tickers_full_data['Three Months Return'] = all_three_months_returns
    tickers_full_data['One Year Return'] = all_one_year_returns

    # revenue
    for i in range(11):
        tickers_full_data[f'Revenue {i+int(2013)}'] = []

    for i in range(11):
        tickers_full_data[f'Gross Profit {i+int(2013)}'] = []

    # op income
    for i in range(11):
        tickers_full_data[f'Op Income {i+int(2013)}'] = []

    # ebit
    for i in range(11):
        tickers_full_data[f'EBIT {i+int(2013)}'] = []

    # net income
    for i in range(11):
        tickers_full_data[f'Net Income {i+int(2013)}'] = []

    # normalized net incom
    for i in range(11):
        tickers_full_data[f'Norm Net Income {i+int(2013)}'] = []

    # sga
    for i in range(11):
        tickers_full_data[f'SGA {i+int(2013)}'] = []

    # r and d
    for i in range(11):
        tickers_full_data[f'R & D {i+int(2013)}'] = []

    # d and a
    for i in range(11):
        tickers_full_data[f'D & A {i+int(2013)}'] = []

    for i in range(11):
        tickers_full_data[f'Cash {i+int(2013)}'] = []

    # short inv
    for i in range(11):
        tickers_full_data[f'Short Inv {i+int(2013)}'] = []

    # long inv
    for i in range(11):
        tickers_full_data[f'Long Inv {i+int(2013)}'] = []

    # inventory
    for i in range(11):
        tickers_full_data[f'Inventory {i+int(2013)}'] = []

    # receivables
    for i in range(11):
        tickers_full_data[f'Receivables {i+int(2013)}'] = []

    # total current assets
    for i in range(11):
        tickers_full_data[f'Total Current Assets {i+int(2013)}'] = []

    # pp and e
    for i in range(11):
        tickers_full_data[f'PP & E {i+int(2013)}'] = []

    # goodwill
    for i in range(11):
        tickers_full_data[f'Goodwill {i+int(2013)}'] = []

    for i in range(11):
        tickers_full_data[f'Total Assets {i+int(2013)}'] = []

    # accounts payable
    for i in range(11):
        tickers_full_data[f'Payables {i+int(2013)}'] = []

    for i in range(11):
        tickers_full_data[f'Current Liabilities {i+int(2013)}'] = []

    # long term debt
    for i in range(11):
        tickers_full_data[f'Long Debt {i+int(2013)}'] = []


    for i in range(11):
        tickers_full_data[f'Total Liabilities {i+int(2013)}'] = []

    # retained earnings
    for i in range(11):
        tickers_full_data[f'Retained E {i+int(2013)}'] = []

    # treasury stocks
    for i in range(11):
        tickers_full_data[f'Treasury Stocks {i+int(2013)}'] = []

    # total equity
    for i in range(11):
        tickers_full_data[f'Total Equity {i+int(2013)}'] = []

    # total liabilities and equity
    for i in range(11):
        tickers_full_data[f'Total Liabilities and Equity {i+int(2013)}'] = []

    # tangible book value
    for i in range(11):
        tickers_full_data[f'Book Value {i+int(2013)}'] = []

    # cash from operations
    for i in range(11):
        tickers_full_data[f'Cash From Operations {i+int(2013)}'] = []

    # cash from investing
    for i in range(11):
        tickers_full_data[f'Cash From Investing {i+int(2013)}'] = []

    # cash from financing
    for i in range(11):
        tickers_full_data[f'Cash From Financing {i+int(2013)}'] = []

    # net changes in cash
    for i in range(11):
        tickers_full_data[f'Net Changes in Cash {i+int(2013)}'] = []




    for revenue_list in all_revenue_lists:
        for i in range(11):
            tickers_full_data[f'Revenue {i+int(2013)}'].append(revenue_list[i])

    for gp_list in all_gross_profit_lists:
        # gp_list = ['NA', 'NA', 'NA', 'NA', 'NA', 'NA', 'NA', 'NA', '0.5 M', '0.4 M', '0.1 M']
        for i in range(11):
            tickers_full_data[f'Gross Profit {i+int(2013)}'].append(gp_list[i])

    for op_income_list in all_op_income_lists:
        for i in range(11):
            tickers_full_data[f'Op Income {i+int(2013)}'].append(op_income_list[i])

    for ebit_list in all_ebit_lists:
        for i in range(11):
            tickers_full_data[f'EBIT {i+int(2013)}'].append(ebit_list[i])

    for net_income_list in all_net_income_lists:
        for i in range(11):
            tickers_full_data[f'Net Income {i+int(2013)}'].append(net_income_list[i])

    for normalized_net_income_list in all_normalized_net_income_lists:
        for i in range(11):
            tickers_full_data[f'Norm Net Income {i+int(2013)}'].append(normalized_net_income_list[i])

    for sga_list in all_sga_lists:
        for i in range(11):
            tickers_full_data[f'SGA {i+int(2013)}'].append(sga_list[i])

    for r_and_d_list in all_r_and_d_lists:
        for i in range(11):
            tickers_full_data[f'R & D {i+int(2013)}'].append(r_and_d_list[i])

    for d_and_a_list in all_d_and_a_lists:
        for i in range(11):
            tickers_full_data[f'D & A {i+int(2013)}'].append(d_and_a_list[i])

    for cash_list in all_cash_lists:
        for i in range(11):
            tickers_full_data[f'Cash {i+int(2013)}'].append(cash_list[i])

    for short_inv_list in all_short_inv_lists:
        for i in range(11):
            tickers_full_data[f'Short Inv {i+int(2013)}'].append(short_inv_list[i])

    for long_inv_list in all_long_inv_lists:
        for i in range(11):
            tickers_full_data[f'Long Inv {i+int(2013)}'].append(long_inv_list[i])

    for inventory_list in all_inventory_lists:
        for i in range(11):
            tickers_full_data[f'Inventory {i+int(2013)}'].append(inventory_list[i])

    for total_receivables_list in all_total_receivables_lists:
        for i in range(11):
            tickers_full_data[f'Receivables {i+int(2013)}'].append(total_receivables_list[i])

    for total_current_assets_list in all_total_current_assets_lists:
        for i in range(11):
            tickers_full_data[f'Total Current Assets {i+int(2013)}'].append(total_current_assets_list[i])

    for pp_and_e_list in all_pp_and_e_lists:
        for i in range(11):
            tickers_full_data[f'PP & E {i+int(2013)}'].append(pp_and_e_list[i])

    for goodwill_list in all_goodwill_lists:
        for i in range(11):
            tickers_full_data[f'Goodwill {i+int(2013)}'].append(goodwill_list[i])

    for total_assets_list in all_total_assets_lists:
        for i in range(11):
            tickers_full_data[f'Total Assets {i+int(2013)}'].append(
                total_assets_list[i])

    for accounts_payable_list in all_accounts_payable_lists:
        for i in range(11):
            tickers_full_data[f'Payables {i+int(2013)}'].append(accounts_payable_list[i])

    for current_liabilities_list in all_current_liabilites_lists:
        for i in range(11):
            tickers_full_data[f'Current Liabilities {i+int(2013)}'].append(
                current_liabilities_list[i])

    for long_debt_list in all_long_debt_lists:
        for i in range(11):
            tickers_full_data[f'Long Debt {i+int(2013)}'].append(long_debt_list[i])

    for total_liabilities_list in all_total_liabilities_lists:
        for i in range(11):
            tickers_full_data[f'Total Liabilities {i+int(2013)}'].append(
                total_liabilities_list[i])

    for retained_earnings_list in all_retained_earnings_lists:
        for i in range(11):
            tickers_full_data[f'Retained E {i+int(2013)}'].append(retained_earnings_list[i])

    for treasury_stock_list in all_treasury_stock_lists:
        for i in range(11):
            tickers_full_data[f'Treasury Stocks {i+int(2013)}'].append(treasury_stock_list[i])

    for total_equity_list in all_total_equity_lists:
        for i in range(11):
            tickers_full_data[f'Total Equity {i+int(2013)}'].append(total_equity_list[i])

    for total_liabilities_and_equity_list in all_total_liabilities_and_equity_lists:
        for i in range(11):
            tickers_full_data[f'Total Liabilities and Equity {i+int(2013)}'].append(total_liabilities_and_equity_list[i])

    for tangible_book_value_list in all_tangible_book_value_lists:
        for i in range(11):
            tickers_full_data[f'Book Value {i+int(2013)}'].append(tangible_book_value_list[i])

    for cash_from_operations_list in all_cash_from_operations_lists:
        for i in range(11):
            tickers_full_data[f'Cash From Operations {i+int(2013)}'].append(cash_from_operations_list[i])

    for cash_from_investing_list in all_cash_from_investing_lists:
        for i in range(11):
            tickers_full_data[f'Cash From Investing {i+int(2013)}'].append(cash_from_investing_list[i])

    for cash_from_financing_list in all_cash_from_financing_lists:
        for i in range(11):
            tickers_full_data[f'Cash From Financing {i+int(2013)}'].append(cash_from_financing_list[i])

    for net_changes_in_cash_list in all_net_changes_in_cash_lists:
        for i in range(11):
            tickers_full_data[f'Net Changes in Cash {i+int(2013)}'].append(net_changes_in_cash_list[i])

    return tickers_full_data

# constant url for income statement and balance sheet
web_page_url = "https://app.koyfin.com"
income_statement_url = "fa/00000000-3c6b-403d-8336-0c36676ca980"
balance_sheet_url = "fa/00000000-6917-48b7-95f0-0d8b144e0f23"
cash_flow_statement_url = "fa/00000000-1c82-4912-88c6-8689b285ac75"


chrome_driver_path = "D://selenium project/chromedriver_win32/chromedriver.exe"
driver = webdriver.Chrome(executable_path=chrome_driver_path)
driver.maximize_window()
# read stock ids file

# get ticker ids from Stock Links folder
ids_df = pd.read_excel('D://selenium project/selenium/Stock Links/9-India/Ticker ids.xlsx')
'''
  ids_df
0  eq-srx148
1  eq-hjfnvd
2  eq-yyo09x
3  eq-66lbjt
4  eq-pljn2m
'''
ticker_ids = list(ids_df['ticker_ids'])

scraped_ids = get_scraped_ids()
new_ids = []
scrape_limit = 9
scrape_counter = 0

# lists to store in excel
all_ticker_symbols = []
all_company_names = []
all_industries = []
all_sectors = []
all_currencies = []
all_market_capitals = []
all_one_year_returns = []
all_three_months_returns = []


all_gross_profit_lists = []

all_revenue_lists = []
all_op_income_lists = []
all_net_income_lists = []
all_ebit_lists = []
all_normalized_net_income_lists = []
all_sga_lists = []
all_r_and_d_lists = []
all_d_and_a_lists = []

all_cash_lists = []
all_total_assets_lists = []
all_current_liabilites_lists = []
all_total_liabilities_lists = []

all_short_inv_lists = []
all_total_receivables_lists = []
all_inventory_lists = []
all_total_current_assets_lists = []
all_long_inv_lists = []
all_long_debt_lists = []
all_goodwill_lists = []
all_retained_earnings_lists = []
all_accounts_payable_lists = []
all_treasury_stock_lists = []
all_total_equity_lists = []
all_total_liabilities_and_equity_lists = []
all_tangible_book_value_lists = []
all_pp_and_e_lists = []

all_cash_from_operations_lists = []
all_cash_from_investing_lists = []
all_cash_from_financing_lists = []
all_net_changes_in_cash_lists = []


# go to koyfin home page
driver.get('https://app.koyfin.com')
# wait to have time to login manually and install CORS extension
sleep(60)


# main program loop
try:
    for id in ticker_ids:
        # if id is not scraped in the past
        if id not in scraped_ids:
            # get income statement and balance sheet urls for current id
            ticker_income_statement = web_page_url + '/' + income_statement_url + '/' + id
            ticker_balance_sheet = web_page_url + '/' + balance_sheet_url + '/' + id
            ticker_cash_flow_statement = web_page_url + '/' + cash_flow_statement_url + '/' + id

            # ------------------------------Income Statement------------------------------------
            symbol = 'NA'
            company_name = 'NA'
            sector = 'NA'
            industry = 'NA'

            currency = "NA"
            mc = 'NA'
            one_year_return = "NA"
            three_months_return = "NA"
            first_fiscal_year = 'NA'

            gp_list = []

            revenue_list = [] # done
            op_income_list = [] # done
            net_income_list = [] # done
            ebit_list = [] # done
            normalized_net_income_list = [] # done
            sga_list = [] # done
            r_and_d_list = [] # done
            d_and_a_list = [] # done
            
            try:
                driver.get(ticker_income_statement)
            except:
                sleep(60)
                try:
                    driver.get(ticker_income_statement)
                except:
                    print(f'==========Failed to load ticker income statement with ID: {id}==========')
                    continue
            # sleep 2 seconds to ensure page is loaded
            sleep(10)

            # scrape ticker symbol
            try:
                symbol = driver.find_element(By.XPATH, '//span[@class="quote-box__ticker___YsyTL"]').text
            except:
                print(f'Failed to extract ticker symbol with ID: {id}')
                pass

            # scrape company name
            try:
                company_name = driver.find_element(By.XPATH, '//div[@class="quote-box__securityName___XtQtz"]').text
            except:
                print(f'Failed to extract ticker company name with ID: {id}')
                pass

            # scrape three months return
            try:
                three_months_return = driver.find_element(By.XPATH, '//div[@class="quote-box__boxLabel___I6TSA"][text()="Total Return (3M)"]/preceding-sibling::div/div/div/div').text
                print(f"=========three months return: {three_months_return}============")
            except:
                print(f'Failed to extract ticker three months return with ID: {id}')
                pass

            # scrape one year return
            try:
                one_year_return = driver.find_element(By.XPATH, '//div[@class="quote-box__boxLabel___I6TSA"][text()="Total Return (1Y)"]/preceding-sibling::div/div/div/div').text
                print(f"=========one year return: {one_year_return}============")
            except:
                print(f'Failed to extract ticker one year return with ID: {id}')
                pass


            # scrape gross profits
            gp_boxes = driver.find_elements(By.XPATH, '//div[@class="fa-table__defaultCell__label___oDEly default-cell__label___x4_Ck"][text()="Gross Profit (Loss)"]//parent::div//parent::div//parent::div/following-sibling::div')
            for box in gp_boxes:
                try:
                    gp_value = box.find_element(By.XPATH, './div/div/div').text
                    gp_scale = box.find_element(By.XPATH, './div/div/span').text
                    gp_list.append(gp_value + ' ' + gp_scale)
                except:
                    gp_list.append('NA')
            gp_list = resize(gp_list)

            
            #//i[@class="primary-button__icon___g7tTE fas fa-coins primary-button__small___O7tuv"]/following-sibling::span
            # scrape currency
            try:
                currency = driver.find_element(By.XPATH, '//i[@class="primary-button__icon___g7tTE fas fa-coins primary-button__small___O7tuv"]/following-sibling::span').text
            except:
                pass
            
            
            
            
            # scrape market capital
            try:
                mc_currency = driver.find_element(By.XPATH, '//span[@class="default-cell__prefix___KFSbr"]').text
                mc_value = driver.find_element(By.XPATH, '//span[@class="default-cell__prefix___KFSbr"]/parent::div').text.split('\n')[1]
                mc_scale = driver.find_element(By.XPATH, '//span[@class="default-cell__prefix___KFSbr"]//parent::div/following-sibling::span').text
                mc = mc_currency + ' ' + mc_value + ' ' + mc_scale
            except:
                pass

            # scrape sector
            try:
                sector = driver.find_element(By.XPATH, '//div[@class="quote-box__boxLabel___I6TSA"][text()="Sector"]/preceding-sibling::div/div/div').text
            except:
                pass

            # scrape industry
            try:
                industry = driver.find_element(By.XPATH, '//div[@class="quote-box__boxLabel___I6TSA"][text()="Industry"]/preceding-sibling::div/div/div').text
            except:
                pass

            # scrape revenues
            revenue_boxes = driver.find_elements(By.XPATH, '//div[@class="fa-table__defaultCell__label___oDEly default-cell__label___x4_Ck"][text()="Total Revenues"]//parent::div//parent::div//parent::div/following-sibling::div')
            for box in revenue_boxes:
                try:
                    revenue_value = box.find_element(By.XPATH, './div/div/div').text
                    revenue_scale = box.find_element(By.XPATH, './div/div/span').text
                    revenue_list.append(revenue_value + ' ' + revenue_scale)
                except:
                    revenue_list.append('NA')
            revenue_list = resize(revenue_list)

            # scrape op income
            op_income_boxes = driver.find_elements(By.XPATH, '//div[@class="fa-table__defaultCell__label___oDEly default-cell__label___x4_Ck"][text()="Operating Income"]//parent::div//parent::div//parent::div/following-sibling::div')
            for box in op_income_boxes:
                try:
                    op_income_value = box.find_element(By.XPATH, './div/div/div').text
                    op_income_scale = box.find_element(By.XPATH, './div/div/span').text
                    op_income_list.append(op_income_value + ' ' + op_income_scale)
                except:
                    op_income_list.append('NA')
            op_income_list = resize(op_income_list)

            # scrape net income
            net_income_boxes = driver.find_elements(By.XPATH, '//div[@class="fa-table__defaultCell__label___oDEly default-cell__label___x4_Ck"][text()="Net Income"]//parent::div//parent::div//parent::div/following-sibling::div')
            for box in net_income_boxes:
                try:
                    net_income_value = box.find_element(By.XPATH, './div/div/div').text
                    net_income_scale = box.find_element(By.XPATH, './div/div/span').text
                    net_income_list.append(
                        net_income_value + ' ' + net_income_scale)
                except:
                    net_income_list.append('NA')
            net_income_list = resize(net_income_list)

            # scrape ebit
            ebit_boxes = driver.find_elements(By.XPATH, '//div[@class="fa-table__defaultCell__label___oDEly default-cell__label___x4_Ck"][text()="EBIT"]//parent::div//parent::div//parent::div/following-sibling::div')
            for box in ebit_boxes:
                try:
                    ebit_value = box.find_element(By.XPATH, './div/div/div').text
                    ebit_scale = box.find_element(By.XPATH, './div/div/span').text
                    ebit_list.append(ebit_value + ' ' + ebit_scale)
                except:
                    ebit_list.append('NA')
            ebit_list = resize(ebit_list)

            # scrape normalized net income
            normalized_net_income_boxes = driver.find_elements(By.XPATH, '//div[@class="fa-table__defaultCell__label___oDEly default-cell__label___x4_Ck"][text()="Normalized Net Income"]//parent::div//parent::div//parent::div/following-sibling::div')
            for box in normalized_net_income_boxes:
                try:
                    normalized_net_income_value = box.find_element(By.XPATH, './div/div/div').text
                    normalized_net_income_scale = box.find_element(By.XPATH, './div/div/span').text
                    normalized_net_income_list.append(normalized_net_income_value + ' ' + normalized_net_income_scale)
                except:
                    normalized_net_income_list.append('NA')
            normalized_net_income_list = resize(normalized_net_income_list)

            # scrape sga
            sga_boxes = driver.find_elements(By.XPATH, '//div[@class="fa-table__defaultCell__label___oDEly default-cell__label___x4_Ck"][text()="Selling General & Admin Expenses"]//parent::div//parent::div//parent::div/following-sibling::div')
            for box in sga_boxes:
                try:
                    sga_value = box.find_element(By.XPATH, './div/div/div').text
                    sga_scale = box.find_element(By.XPATH, './div/div/span').text
                    sga_list.append(sga_value + ' ' + sga_scale)
                except:
                    sga_list.append('NA')
            sga_list = resize(sga_list)

            # scrape r_and_d
            r_and_d_boxes = driver.find_elements(By.XPATH, '//div[@class="fa-table__defaultCell__label___oDEly default-cell__label___x4_Ck"][text()="R&D Expenses"]//parent::div//parent::div//parent::div/following-sibling::div')
            for box in r_and_d_boxes:
                try:
                    r_and_d_value = box.find_element(By.XPATH, './div/div/div').text
                    r_and_d_scale = box.find_element(By.XPATH, './div/div/span').text
                    r_and_d_list.append(r_and_d_value + ' ' + r_and_d_scale)
                except:
                    r_and_d_list.append('NA')
            r_and_d_list = resize(r_and_d_list)

            # scrape d_and_a
            d_and_a_boxes = driver.find_elements(By.XPATH, '//div[@class="fa-table__defaultCell__label___oDEly default-cell__label___x4_Ck"][text()="Depreciation & Amortization "]//parent::div//parent::div//parent::div/following-sibling::div')
            for box in d_and_a_boxes:
                try:
                    d_and_a_value = box.find_element(By.XPATH, './div/div/div').text
                    d_and_a_scale = box.find_element(By.XPATH, './div/div/span').text
                    d_and_a_list.append(d_and_a_value + ' ' + d_and_a_scale)
                except:
                    d_and_a_list.append('NA')
            d_and_a_list = resize(d_and_a_list)



            print(f"Scrape #{scrape_counter}")
            print(f"Ticker: {symbol}")
            print(f"Company Name: {company_name}")
            print(f"One Year Return: {one_year_return}")
            print(f"Three Months Return: {three_months_return}")
            print(f"Industry: {industry}")
            print(f"Sector: {sector}")
            print(f"Currency: {currency}")
            print(f"MC: {mc}")
            print(f"GP: {gp_list}")
            print(f'first FY: {first_fiscal_year}')
            
            print(f'revenue_list: {revenue_list}')
            print(f'op_income_list: {op_income_list}')
            print(f'net_income_list: {net_income_list}')
            print(f'ebit_list: {ebit_list}')
            print(f'normalized_net_income_list: {normalized_net_income_list}')
            print(f'sga_list: {sga_list}')
            print(f'r_and_d_list: {r_and_d_list}')
            print(f'd_and_a_list: {d_and_a_list}')
            print()

            # ------------------------------Balance Sheet------------------------------------
            total_assets_list = []
            total_liabilities_list = []
            cash_list = []
            current_liabilities_list = []

            short_inv_list = [] # done
            total_receivables_list = [] # done
            inventory_list = [] # done
            total_current_assets_list = [] # done
            long_inv_list = [] # done
            long_debt_list = [] # done
            goodwill_list = [] # done
            retained_earnings_list = [] # done
            accounts_payable_list = [] # done
            treasury_stock_list = [] # done
            total_equity_list = [] # done
            total_liabilities_and_equity_list = [] # done
            tangible_book_value_list = [] # done
            pp_and_e_list = [] # done
            
            try:
                driver.get(ticker_balance_sheet)
            except:
                sleep(60)
                try:
                    driver.get(ticker_balance_sheet)
                except:
                    print(f'==========Failed to load ticker balance sheet with ID: {id}==========')
                    continue
            # sleep 2 seconds to ensure page is loaded
            sleep(10)

            # scrape total assets
            total_asset_boxes = driver.find_elements(By.XPATH, '//div[@class="fa-table__defaultCell__label___oDEly default-cell__label___x4_Ck"][text()="Total Assets"]//parent::div//parent::div//parent::div/following-sibling::div')
            for box in total_asset_boxes:
                try:
                    total_asset_value = box.find_element(By.XPATH, './div/div/div').text
                    total_asset_scale = box.find_element(By.XPATH, './div/div/span').text
                    total_assets_list.append(total_asset_value + ' ' + total_asset_scale)

                except:
                    total_assets_list.append('NA')
            total_assets_list = resize(total_assets_list)

            # scrape cash
            cash_boxes = driver.find_elements(By.XPATH, '//div[@class="fa-table__defaultCell__label___oDEly default-cell__label___x4_Ck"][text()="Cash And Equivalents"]/parent::div/parent::div/parent::div/following-sibling::div')
            for box in cash_boxes:
                try:
                    cash_value = box.find_element(By.XPATH, './div/div/div').text
                    cash_scale = box.find_element(By.XPATH, './div/div/span').text
                    cash_list.append(cash_value + ' ' + cash_scale)
                except:
                    cash_list.append('NA')
            cash_list = resize(cash_list)

            # scrape total liabilites
            total_liabilities_boxes = driver.find_elements(By.XPATH, '//div[@class="fa-table__defaultCell__label___oDEly default-cell__label___x4_Ck"][text()="Total Liabilities"]/parent::div/parent::div/parent::div/following-sibling::div')
            for box in total_liabilities_boxes:
                try:
                    total_liabilities_value = box.find_element(By.XPATH, './div/div/div').text
                    total_liabilities_scale = box.find_element(By.XPATH, './div/div/span').text
                    total_liabilities_list.append(total_liabilities_value + ' ' + total_liabilities_scale)
                except:
                    total_liabilities_list.append('NA')
            total_liabilities_list = resize(total_liabilities_list)

            # scrape current liabilites
            current_liabilities_boxes = driver.find_elements(
                By.XPATH, '//div[@class="fa-table__defaultCell__label___oDEly default-cell__label___x4_Ck"][text()="Total Current Liabilities"]/parent::div/parent::div/parent::div/following-sibling::div')
            for box in current_liabilities_boxes:
                try:
                    current_liabilities_value = box.find_element(By.XPATH, './div/div/div').text
                    current_liabilities_scale = box.find_element(By.XPATH, './div/div/span').text
                    current_liabilities_list.append(current_liabilities_value + ' ' + current_liabilities_scale)
                except:
                    current_liabilities_list.append('NA')
            current_liabilities_list = resize(current_liabilities_list)

            # scrape short term investments
            short_inv_boxes = driver.find_elements(By.XPATH, '//div[@class="fa-table__defaultCell__label___oDEly default-cell__label___x4_Ck"][text()="Short Term Investments"]/parent::div/parent::div/parent::div/following-sibling::div')
            for box in short_inv_boxes:
                try:
                    short_inv_value = box.find_element(By.XPATH, './div/div/div').text
                    short_inv_scale = box.find_element(By.XPATH, './div/div/span').text
                    short_inv_list.append(short_inv_value + ' ' + short_inv_scale)
                except:
                    short_inv_list.append('NA')
            short_inv_list = resize(short_inv_list)

            # scrape total receivables
            total_receivables_boxes = driver.find_elements(By.XPATH, '//div[@class="fa-table__defaultCell__label___oDEly default-cell__label___x4_Ck"][text()="Total Receivables"]/parent::div/parent::div/parent::div/following-sibling::div')
            for box in total_receivables_boxes:
                try:
                    total_receivables_value = box.find_element(By.XPATH, './div/div/div').text
                    total_receivables_scale = box.find_element(By.XPATH, './div/div/span').text
                    total_receivables_list.append(total_receivables_value + ' ' + total_receivables_scale)
                except:
                    total_receivables_list.append('NA')
            total_receivables_list = resize(total_receivables_list)

            # scrape inventory
            inventory_boxes = driver.find_elements(By.XPATH, '//div[@class="fa-table__defaultCell__label___oDEly default-cell__label___x4_Ck"][text()="Inventory"]/parent::div/parent::div/parent::div/following-sibling::div')
            for box in inventory_boxes:
                try:
                    inventory_value = box.find_element(By.XPATH, './div/div/div').text
                    inventory_scale = box.find_element(By.XPATH, './div/div/span').text
                    inventory_list.append(inventory_value + ' ' + inventory_scale)
                except:
                    inventory_list.append('NA')
            inventory_list = resize(inventory_list)

            # scrape total current assets
            total_current_assets_boxes = driver.find_elements(By.XPATH, '//div[@class="fa-table__defaultCell__label___oDEly default-cell__label___x4_Ck"][text()="Total Current Assets"]/parent::div/parent::div/parent::div/following-sibling::div')
            for box in total_current_assets_boxes:
                try:
                    total_current_assets_value = box.find_element(By.XPATH, './div/div/div').text
                    total_current_assets_scale = box.find_element(By.XPATH, './div/div/span').text
                    total_current_assets_list.append(total_current_assets_value + ' ' + total_current_assets_scale)
                except:
                    total_current_assets_list.append('NA')
            total_current_assets_list = resize(total_current_assets_list)

            # scrape long term investments
            long_inv_boxes = driver.find_elements(By.XPATH, '//div[@class="fa-table__defaultCell__label___oDEly default-cell__label___x4_Ck"][text()="Long-term Investments"]/parent::div/parent::div/parent::div/following-sibling::div')
            for box in long_inv_boxes:
                try:
                    long_inv_value = box.find_element(By.XPATH, './div/div/div').text
                    long_inv_scale = box.find_element(By.XPATH, './div/div/span').text
                    long_inv_list.append(long_inv_value + ' ' + long_inv_scale)
                except:
                    long_inv_list.append('NA')
            long_inv_list = resize(long_inv_list)

            # scrape long term debt
            long_debt_boxes = driver.find_elements(By.XPATH, '//div[@class="fa-table__defaultCell__label___oDEly default-cell__label___x4_Ck"][text()="Long-Term Debt"]/parent::div/parent::div/parent::div/following-sibling::div')
            for box in long_debt_boxes:
                try:
                    long_debt_value = box.find_element(By.XPATH, './div/div/div').text
                    long_debt_scale = box.find_element(By.XPATH, './div/div/span').text
                    long_debt_list.append(long_debt_value + ' ' + long_debt_scale)
                except:
                    long_debt_list.append('NA')
            long_debt_list = resize(long_debt_list)

            # scrape goodwill
            goodwill_boxes = driver.find_elements(By.XPATH, '//div[@class="fa-table__defaultCell__label___oDEly default-cell__label___x4_Ck"][text()="Goodwill"]/parent::div/parent::div/parent::div/following-sibling::div')
            for box in goodwill_boxes:
                try:
                    goodwill_value = box.find_element(By.XPATH, './div/div/div').text
                    goodwill_scale = box.find_element(By.XPATH, './div/div/span').text
                    goodwill_list.append(goodwill_value + ' ' + goodwill_scale)
                except:
                    goodwill_list.append('NA')
            goodwill_list = resize(goodwill_list)

            # scrape retained earnings
            retained_earnings_boxes = driver.find_elements(By.XPATH, '//div[@class="fa-table__defaultCell__label___oDEly default-cell__label___x4_Ck"][text()="Retained Earnings"]/parent::div/parent::div/parent::div/following-sibling::div')
            for box in retained_earnings_boxes:
                try:
                    retained_earnings_value = box.find_element(By.XPATH, './div/div/div').text
                    retained_earnings_scale = box.find_element(By.XPATH, './div/div/span').text
                    retained_earnings_list.append(retained_earnings_value + ' ' + retained_earnings_scale)
                except:
                    retained_earnings_list.append('NA')
            retained_earnings_list = resize(retained_earnings_list)

            # scraper accounts payable
            accounts_payable_boxes = driver.find_elements(By.XPATH, '//div[@class="fa-table__defaultCell__label___oDEly default-cell__label___x4_Ck"][text()="Accounts Payable"]/parent::div/parent::div/parent::div/following-sibling::div')
            for box in accounts_payable_boxes:
                try:
                    accounts_payable_value = box.find_element(By.XPATH, './div/div/div').text
                    accounts_payable_scale = box.find_element(By.XPATH, './div/div/span').text
                    accounts_payable_list.append(accounts_payable_value + ' ' + accounts_payable_scale)
                except:
                    accounts_payable_list.append('NA')
            accounts_payable_list = resize(accounts_payable_list)

            # scrape treasury stock
            treasury_stock_boxes = driver.find_elements(By.XPATH, '//div[@class="fa-table__defaultCell__label___oDEly default-cell__label___x4_Ck"][text()="Treasury Stock"]/parent::div/parent::div/parent::div/following-sibling::div')
            for box in treasury_stock_boxes:
                try:
                    treasury_stock_value = box.find_element(By.XPATH, './div/div/div').text
                    treasury_stock_scale = box.find_element(By.XPATH, './div/div/span').text
                    treasury_stock_list.append(treasury_stock_value + ' ' + treasury_stock_scale)
                except:
                    treasury_stock_list.append('NA')
            treasury_stock_list = resize(treasury_stock_list)

            # scrape total equity
            total_equity_boxes = driver.find_elements(By.XPATH, '//div[@class="fa-table__defaultCell__label___oDEly default-cell__label___x4_Ck"][text()="Total Equity"]/parent::div/parent::div/parent::div/following-sibling::div')
            for box in total_equity_boxes:
                try:
                    total_equity_value = box.find_element(By.XPATH, './div/div/div').text
                    total_equity_scale = box.find_element(By.XPATH, './div/div/span').text
                    total_equity_list.append(total_equity_value + ' ' + total_equity_scale)
                except:
                    total_equity_list.append('NA')
            total_equity_list = resize(total_equity_list)

            # scrape total liabilities and equity
            total_liabilities_and_equity_boxes = driver.find_elements(By.XPATH, '//div[@class="fa-table__defaultCell__label___oDEly default-cell__label___x4_Ck"][text()="Total Liabilities And Equity"]/parent::div/parent::div/parent::div/following-sibling::div')
            for box in total_liabilities_and_equity_boxes:
                try:
                    total_liabilities_and_equity_value = box.find_element(By.XPATH, './div/div/div').text
                    total_liabilities_and_equity_scale = box.find_element(By.XPATH, './div/div/span').text
                    total_liabilities_and_equity_list.append(total_liabilities_and_equity_value + ' ' + total_liabilities_and_equity_scale)
                except:
                    total_liabilities_and_equity_list.append('NA')
            total_liabilities_and_equity_list = resize(total_liabilities_and_equity_list)

            # scrape tangible book value
            tangible_book_value_boxes = driver.find_elements(By.XPATH, '//div[@class="fa-table__defaultCell__label___oDEly default-cell__label___x4_Ck"][text()="Tangible Book Value"]/parent::div/parent::div/parent::div/following-sibling::div')
            for box in tangible_book_value_boxes:
                try:
                    tangible_book_value_value = box.find_element(By.XPATH, './div/div/div').text
                    tangible_book_value_scale = box.find_element(By.XPATH, './div/div/span').text
                    tangible_book_value_list.append(tangible_book_value_value + ' ' + tangible_book_value_scale)
                except:
                    tangible_book_value_list.append('NA')
            tangible_book_value_list = resize(tangible_book_value_list)

            # scrape pp and t
            pp_and_e_boxes = driver.find_elements(By.XPATH, '//div[@class="fa-table__defaultCell__label___oDEly default-cell__label___x4_Ck"][text()="Net Property Plant And Equipment"]/parent::div/parent::div/parent::div/following-sibling::div')
            for box in pp_and_e_boxes:
                try:
                    pp_and_e_value = box.find_element(By.XPATH, './div/div/div').text
                    pp_and_e_scale = box.find_element(By.XPATH, './div/div/span').text
                    pp_and_e_list.append(pp_and_e_value + ' ' + pp_and_e_scale)
                except:
                    pp_and_e_list.append('NA')
            pp_and_e_list = resize(pp_and_e_list)

            print(f"Total Assets: {total_assets_list}")
            print(f"Cash: {cash_list}")
            print(f"Total Liabilities: {total_liabilities_list}")
            print(f"Curren Liabilities: {current_liabilities_list}")

            print(f"short_inv_list: {short_inv_list}")
            print(f"total_receivables_list: {total_receivables_list}")
            print(f"inventory_list: {inventory_list}")
            print(f"total_current_assets_list: {total_current_assets_list}")
            print(f"long_inv_list: {long_inv_list}")
            print(f"long_debt_list: {long_debt_list}")
            print(f"goodwill_list: {goodwill_list}")
            print(f"retained_earnings_list: {retained_earnings_list}")
            print(f"accounts_payable_list: {accounts_payable_list}")
            print(f"treasury_stock_list: {treasury_stock_list}")
            print(f"total_equity_list: {total_equity_list}")
            print(f"total_liabilities_and_equity_list: {total_liabilities_and_equity_list}")
            print(f"tangible_book_value_list: {tangible_book_value_list}")
            print(f"pp_and_e_list: {pp_and_e_list}")
            print()

            # ------------------------------Cash Flow Statement------------------------------------
            cash_from_operations_list = []
            cash_from_investing_list = []
            cash_from_financing_list = []
            net_changes_in_cash_list = []

            # go to cash flow statement page
            try:
                driver.get(ticker_cash_flow_statement)
            except:
                sleep(60)
                try:
                    driver.get(ticker_cash_flow_statement)
                except:
                    print(f'==========Failed to load ticker cash flow statement with ID: {id}==========')
                    continue
            # wait for page to load completely
            sleep(10)

            # scrape cash from operations
            cash_from_operations_boxes = driver.find_elements(By.XPATH, '//div[@class="fa-table__defaultCell__label___oDEly default-cell__label___x4_Ck"][text()="Cash from Operations"]//parent::div//parent::div//parent::div/following-sibling::div')
            for box in cash_from_operations_boxes:
                try:
                    cash_from_operations_value = box.find_element(By.XPATH, './div/div/div').text
                    cash_from_operations_scale = box.find_element(By.XPATH, './div/div/span').text
                    cash_from_operations_list.append(cash_from_operations_value + ' ' + cash_from_operations_scale)

                except:
                    cash_from_operations_list.append('NA')
            cash_from_operations_list = resize(cash_from_operations_list)

            # scrape cash from investing
            cash_from_investing_boxes = driver.find_elements(By.XPATH, '//div[@class="fa-table__defaultCell__label___oDEly default-cell__label___x4_Ck"][text()="Cash from Investing"]//parent::div//parent::div//parent::div/following-sibling::div')
            for box in cash_from_investing_boxes:
                try:
                    cash_from_investing_value = box.find_element(By.XPATH, './div/div/div').text
                    cash_from_investing_scale = box.find_element(By.XPATH, './div/div/span').text
                    cash_from_investing_list.append(cash_from_investing_value + ' ' + cash_from_investing_scale)

                except:
                    cash_from_investing_list.append('NA')
            cash_from_investing_list = resize(cash_from_investing_list)

            # scrape cash from financing
            cash_from_financing_boxes = driver.find_elements(By.XPATH, '//div[@class="fa-table__defaultCell__label___oDEly default-cell__label___x4_Ck"][text()="Cash from Financing"]//parent::div//parent::div//parent::div/following-sibling::div')
            for box in cash_from_financing_boxes:
                try:
                    cash_from_financing_value = box.find_element(By.XPATH, './div/div/div').text
                    cash_from_financing_scale = box.find_element(By.XPATH, './div/div/span').text
                    cash_from_financing_list.append(cash_from_financing_value + ' ' + cash_from_financing_scale)

                except:
                    cash_from_financing_list.append('NA')
            cash_from_financing_list = resize(cash_from_financing_list)

            # scrape net changes in cash
            net_changes_in_cash_boxes = driver.find_elements(By.XPATH, '//div[@class="fa-table__defaultCell__label___oDEly default-cell__label___x4_Ck"][text()="Net Change in Cash"]//parent::div//parent::div//parent::div/following-sibling::div')
            for box in net_changes_in_cash_boxes:
                try:
                    net_changes_in_cash_value = box.find_element(By.XPATH, './div/div/div').text
                    net_changes_in_cash_scale = box.find_element(By.XPATH, './div/div/span').text
                    net_changes_in_cash_list.append(net_changes_in_cash_value + ' ' + net_changes_in_cash_scale)

                except:
                    net_changes_in_cash_list.append('NA')
            net_changes_in_cash_list = resize(net_changes_in_cash_list)

            print(f"cash_from_operations_list: {cash_from_operations_list}")
            print(f"cash_from_investing_list: {cash_from_investing_list}")
            print(f"cash_from_financing_list: {cash_from_financing_list}")
            print(f"net_changes_in_cash_list: {net_changes_in_cash_list}")
            print('----------------------------------------------------------------------')

            # add all stock infos to its related list
            all_ticker_symbols.append(symbol)
            all_company_names.append(company_name)
            if three_months_return:
                all_three_months_returns.append(three_months_return)
            else:
                all_three_months_returns.append("Damn")

            if one_year_return:
                all_one_year_returns.append(one_year_return)
            else:
                all_one_year_returns.append("Damn")
            all_industries.append(industry)
            all_sectors.append(sector)
            all_currencies.append(currency)
            all_market_capitals.append(mc)
            all_gross_profit_lists.append(gp_list)
            all_cash_lists.append(cash_list)
            all_total_assets_lists.append(total_assets_list)
            all_current_liabilites_lists.append(current_liabilities_list)
            all_total_liabilities_lists.append(total_liabilities_list)

            all_revenue_lists.append(revenue_list)# done
            all_op_income_lists.append(op_income_list)# done
            all_net_income_lists.append(net_income_list)# done
            all_ebit_lists.append(ebit_list) # done
            all_normalized_net_income_lists.append(normalized_net_income_list) # done
            all_sga_lists.append(sga_list)# done
            all_r_and_d_lists.append(r_and_d_list) # done
            all_d_and_a_lists.append(d_and_a_list) # done

            all_short_inv_lists.append(short_inv_list) # done
            all_total_receivables_lists.append(total_receivables_list) # done
            all_inventory_lists.append(inventory_list) # done
            all_total_current_assets_lists.append(total_current_assets_list) # done
            all_long_inv_lists.append(long_inv_list) # done
            all_long_debt_lists.append(long_debt_list) # done
            all_goodwill_lists.append(goodwill_list) # done
            all_retained_earnings_lists.append(retained_earnings_list) # done
            all_accounts_payable_lists.append(accounts_payable_list) # done
            all_treasury_stock_lists.append(treasury_stock_list) # done
            all_total_equity_lists.append(total_equity_list) # done
            all_total_liabilities_and_equity_lists.append(total_liabilities_and_equity_list) # done
            all_tangible_book_value_lists.append(tangible_book_value_list)
            all_pp_and_e_lists.append(pp_and_e_list) # done

            all_cash_from_operations_lists.append(cash_from_operations_list)
            all_cash_from_investing_lists.append(cash_from_investing_list)
            all_cash_from_financing_lists.append(cash_from_financing_list)
            all_net_changes_in_cash_lists.append(net_changes_in_cash_list)


            # add to newly scraped ids
            new_ids.append(symbol + ':' + id)
            # increment scraper_counter
            scrape_counter += 1
            
            # check for a 20 batch ticker to append to excel and text file
            if (scrape_counter >= scrape_limit):
                # append data to existing excel file
                previous_data_df = pd.read_excel('D://selenium project/selenium/Stocks Data/9-India/Fiscal Year 2022 Update/Full Data FY2022 Update.xlsx')
                current_data_df = pd.DataFrame(create_main_df_dict())
                df_list = [previous_data_df, current_data_df]
                final_data_df = pd.concat(df_list)
                final_data_df.to_excel('D://selenium project/selenium/Stocks Data/9-India/Fiscal Year 2022 Update/Full Data FY2022 Update.xlsx', index=False, header=True)

                # add newly scraped ids to scraped ids text file
                set_scraped_ids(new_ids)

                # reset variables and lists
                scrape_counter = 0
                new_ids.clear()

                all_ticker_symbols.clear()
                all_company_names.clear()
                all_industries.clear()
                all_sectors.clear()
                all_market_capitals.clear()
                all_currencies.clear()
                all_three_months_returns.clear()
                all_one_year_returns.clear()

                all_gross_profit_lists.clear()

                all_revenue_lists.clear()
                all_op_income_lists.clear()
                all_net_income_lists.clear()
                all_ebit_lists.clear()
                all_normalized_net_income_lists.clear()
                all_sga_lists.clear()
                all_r_and_d_lists.clear()
                all_d_and_a_lists.clear()

                all_cash_lists.clear()
                all_total_assets_lists.clear()
                all_current_liabilites_lists.clear()
                all_total_liabilities_lists.clear()

                all_short_inv_lists.clear()
                all_total_receivables_lists.clear()
                all_inventory_lists.clear()
                all_total_current_assets_lists.clear()
                all_long_inv_lists.clear()
                all_long_debt_lists.clear()
                all_goodwill_lists.clear()
                all_retained_earnings_lists.clear()
                all_accounts_payable_lists.clear()
                all_treasury_stock_lists.clear()
                all_total_equity_lists.clear()
                all_total_liabilities_and_equity_lists.clear()
                all_tangible_book_value_lists.clear()
                all_pp_and_e_lists.clear()

                all_cash_from_operations_lists.clear()
                all_cash_from_investing_lists.clear()
                all_cash_from_financing_lists.clear()
                all_net_changes_in_cash_lists.clear()

except Exception as e:
    print("==========Some error happend and it is caught in the outer exception handler==========")
    print(e)


driver.quit()
