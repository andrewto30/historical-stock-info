################
# Will store all methods used to retrieve stock information
################
from polygon import RESTClient
from polygon import NoResultsError
from polygonAPIKey import polygonAPIkey
import pandas as pd
import datetime

# Connect to Polygon API Key
client = RESTClient(polygonAPIkey)

# Retrieve ticker data
def get_price_data(ticker: str, aggsMult: int, aggs: str, from_, to):

    try:
        # Send request to retrieve info
        data_request = client.get_aggs(ticker=ticker,
                                    multiplier=aggsMult,
                                    timespan=aggs,
                                    from_=from_,
                                    to=to)
        
        # Turn data into a readable table
        price_data = pd.DataFrame(data_request)

        # Timestamp column is in Epoch Unix timestamp so convert to year-month-day format
        price_data['timestamp'] = price_data['timestamp'].apply(lambda x: pd.to_datetime(x*1000000))
        price_data['timestamp'] = price_data['timestamp'].apply(lambda x: x.strftime("%Y-%m-%d"))
        
        return price_data
    
    # Throw exception if there are no results to display
    except NoResultsError:
        print("No results error, please make sure dates are correct along with aggregation inputs")

# Retrieve news data if any 
def get_news_data(ticker: str, date: str):

    # Send news data request
    news_request = client.list_ticker_news(ticker=ticker,
                                           published_utc=date)
    
    # Turn data into readable table
    news_data = pd.DataFrame(news_request)
    
    return news_data

# Get Pre-market data for a specific date; note to use this function from_ and to need to be the same date
def get_pm_data(ticker: str, aggsMult: int, aggs: str, from_, to):

    try:
        # Convert timestamp to milliseconds
        from_ = convert_to_milliseconds(from_ + ' 04:00:00')
        to = convert_to_milliseconds(to + ' 09:29:00')
        
        # Send request to retrieve info
        data_request = client.get_aggs(ticker=ticker,
                                    multiplier=aggsMult,
                                    timespan=aggs,
                                    from_=from_,
                                    to=to)
        
        # Turn data into a readable table
        price_data = pd.DataFrame(data_request)

        # Timestamp column is in Epoch Unix timestamp so convert to year-month-day format
        price_data['timestamp'] = price_data['timestamp'].apply(lambda x: pd.to_datetime(x*1000000))
        price_data['timestamp'] = price_data['timestamp'].apply(lambda x: x.strftime("%Y-%m-%d"))
        
        return price_data
    
    # Throw exception if there are no results to display
    except NoResultsError:
        print("No results error, please make sure dates are correct along with aggregation inputs")

def convert_to_milliseconds(date: str):
    
    # Converter to correct format
    date_str = datetime.datetime.strptime(date, "%Y-%m-%d %H:%M:%S")

    # Convert from datetime to milliseconds
    milliseconds = int(date_str.timestamp() * 1000)

    return milliseconds