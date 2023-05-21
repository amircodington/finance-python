# import yfinance as yf
# import mplfinance as mpf

from utilities import *
from datetime import datetime
from data import Data
from pivot import Pivot
from chart import Chart


today = datetime.today()

symbol = Data('MSFT', start=past_days(today, 180), end=today)
chart = Chart(symbol)
chart.plot_support_resistance()
