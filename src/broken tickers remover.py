# imports
import pandas as pd


def get_corrupted_tickers():
    corrupted_df = pd.read_excel('D://selenium project/selenium/Stocks Data/9-India/Fiscal Year 2022 Update/broken tickers.xlsx')
    temp = list(corrupted_df['ticker'])
    temp = [str(ticker) for ticker in temp] # for China: int() for others str()
    return temp

def remove_ticker(tickers_list):
    '''removes given tickers and their related ids from scraped ids text file'''

    with open('D://selenium project/selenium/Stocks Data/9-India/Fiscal Year 2022 Update/scraped ids.txt') as scraped_file:
        scraped_list = scraped_file.readlines()
        scraped_list = [id[:-1] for id in scraped_list]
        # ['JBHT:eq-7hg374', 'JBLU:eq-q1vxq5', 'JBSS:eq-h3dabt', 'JD:eq-ap7x0z', 'JJSF:eq-rnzl8u', 'JKHY:eq-6s7ysb', 'JNCE:eq-pex643', 'JOUT:eq-wt3i4b', 'KALU:eq-e5odua']
        new_scraped_list = []

        for id in scraped_list:
            if id.split(':')[0] not in tickers_list: # for China: int() for others: nothing
                new_scraped_list.append(id)
        with open('D://selenium project/selenium/Stocks Data/9-India/Fiscal Year 2022 Update/new scraped ids.txt', mode='w') as new_scraped_file:
            for id in new_scraped_list:
                new_scraped_file.write(id + '\n')

corrupted_tickers = get_corrupted_tickers()

# Run Program
print(len(corrupted_tickers))
remove_ticker(corrupted_tickers)

#----------------------corrupted tickers--------------------------