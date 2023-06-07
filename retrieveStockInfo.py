from methodsModule import *

# Set initial ticker information such as symbol, aggregate multiplier, aggregation, to, and from
ticker = 'SHOP'
aggsMult = 1
aggs = 'day'
# For premarket data you will need to aggregations less than daily and the to and from will need to be the same date
pmAggsMult = 30
pmAggs = 'minute'
to = '2023-05-17'
from_ = '2023-05-17'

# Get stock data given parameters from above
price_data = get_price_data(ticker, aggsMult, aggs, from_, to)
pm_data = get_pm_data(ticker, pmAggsMult, pmAggs, from_, to)
news_data = get_news_data(ticker, to)

print(price_data)
print(pm_data)
print(news_data)
