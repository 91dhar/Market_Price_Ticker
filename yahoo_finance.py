import datetime
import yfinance as yf
import platform
print('Python version = ' + platform.python_version())
print('yfinance version = ' + yf.__version__)


def yfinancetut(tickersymbol):
    tickerdata = yf.Ticker(tickersymbol)
    tickerinfo = tickerdata.info
    investment = tickerinfo['shortName']
    print('Investment: ' + investment)

    today = datetime.datetime.today().isoformat()
    print('Today = ' + today)

    tickerDF = tickerdata.history(
        period='1d', start='2022-1-1', end=today[:10])
    priceLast = tickerDF['Close'].iloc[-1]
    priceYest = tickerDF['Close'].iloc[-2]
    change = priceLast - priceYest
    print(investment + ' price last = ' + str(priceLast))
    print('Price Change = ' + str(change))
    print(tickerDF)


yfinancetut('TSLA')  # tesla
print('')
yfinancetut('MANU')  # manchester united
