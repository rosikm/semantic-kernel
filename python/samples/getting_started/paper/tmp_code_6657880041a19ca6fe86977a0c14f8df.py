import yfinance as yf
from datetime import datetime, timedelta

# Define the ticker symbol
tickerSymbol = 'NVDA'

# Get data for the past month
end_date = datetime.strptime('2024-05-09', '%Y-%m-%d')
start_date = end_date - timedelta(days=30)

# Get the data
tickerData = yf.Ticker(tickerSymbol)
tickerDf = tickerData.history(period='1d', start=start_date, end=end_date)

print(tickerDf)