
'''
using data from the top-gainers and market-cap APIs, get the absolute gain in market
cap for the top ten gainers.

write a function that returns a pandas dataframe with columns:
ticker: str
percent_gain: float
absolute_market_cap_gain: float

and ordered by percent_gain descending

Top Gainers API:
Returns the US stocks with the highest percentage gains for today
docs: https://financialmodelingprep.com/developer/docs/most-gainers-stock-market-data-free-api/

Market Capitalization API:
Returns total market capitalization (market cap) for an individual stock from yesterday
docs: https://financialmodelingprep.com/developer/docs/market-capitalization/

curl https://financialmodelingprep.com/api/v3/stock/gainers
'''
import pandas as pd
import json
from datetime import date
from urllib.request import urlopen


def get_jsonparsed_data(url):
    response = urlopen(url)
    data = response.read().decode("utf-8")
    return json.loads(data)

def create_dataframe(data):
    return pd.DataFrame(data)

def remove_unused_columns(df, columns_to_drop):
    return df.drop(columns_to_drop, axis=1)

def get_market_cap(ticker):
    API_KEY = '325b3f0001b699c2a85496e386475e8a'
    MARKET_TOP_GAINERS_API = "https://financialmodelingprep.com/api/v3/market-capitalization/"+ticker+"?apikey=" + API_KEY
    data = get_jsonparsed_data(MARKET_TOP_GAINERS_API)
    if(len(data)>0):
        return data[0]['marketCap']
    return 'NA'

def clear(element):
    return float(element.replace('(','').replace('%','').replace('+','').replace(')',''))

def enrich_dataframe(df,fn,label):
    return df[label].apply(lambda arg: fn(arg) )

def main():
    API_KEY = '325b3f0001b699c2a85496e386475e8a'
    STOCKS_TOP_GAINERS_API = "https://financialmodelingprep.com/api/v3/stock/gainers?apikey=" + API_KEY
    DROPABLE_COLUMNS = ['changes','price','companyName','changesPercentage']
    data = get_jsonparsed_data(STOCKS_TOP_GAINERS_API)['mostGainerStock']
    df = create_dataframe(data)
    df['Ticker'] = enrich_dataframe(df,get_market_cap,'ticker')
    df['Gained'] = enrich_dataframe(df,clear,'changesPercentage')
    df = remove_unused_columns(df,DROPABLE_COLUMNS)
    result = df.sort_values(by = "Gained",ascending=False)

    print(result)
main()