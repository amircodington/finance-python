import yfinance as yf
import numpy as np
from utilities import *
from datetime import datetime
from scipy.signal import argrelextrema, find_peaks


today = datetime.today()

class Data:
    def __init__(self, symbol, start=None, end=None):
        self.symbol = symbol
        self.start = start
        self.end = end
        self.data = self.symbol_data()
    
    #------------ Get data ------------#
    def get_symbol(self):
        return self.symbol
    
    def symbol_data(self):
        print('Fetching data ....') 
        data = yf.download(self.symbol, start=str(self.start.date()), end=str(self.end.date()))
        print('Done!')
        return data
    
    def get_list(self, column):
        result_list = []
        for i, j in self.data[column].items():
            result_list.append(j)
        print('-------------')
        return result_list
    
    def HIGHprev(self):
        high_list = self.get_list('High')
        return high_list[-1]
   
    def LOWprev(self):
        low_list = self.get_list('Low')
        return low_list[-1]
    
    def CLOSEprev(self):
        close_list = self.get_list('Close')
        return close_list[-1]
    
    def show_date_range(self):
        print(f'end_date: {str(self.end.date())}')
        print(f'start_date: {str(self.start.date())}')
    
    #------------ Get points ------------#
    def get_support(self, distance=10):
        # Identify local minima
        minima_indices = find_peaks(-1 * self.data['Close'].values, distance=distance)[0]
        support = self.data['Close'].iloc[minima_indices]
        return support
    
    def get_resistance(self, distance=10):
        # Identify local maxima
        maxima_indices = find_peaks(self.data['Close'].values, distance=distance)[0]
        resistance = self.data['Close'].iloc[maxima_indices]
        return resistance

    def find_pin_bars(self):
        pin_bars = []

        for i in range(len(self.data)):
            row = self.data.iloc[i]
            
            open_price, high, low, close = row['Open'], row['High'], row['Low'], row['Close']
            body = abs(close - open_price)
            candle_range = high - low

            body_in_top_fourth = close > open_price and (high - close) <= 0.25 * candle_range
            body_in_bottom_fourth = close < open_price and (close - low) <= 0.25 * candle_range

            wick_at_least_3x_body = body * 3 <= candle_range

            if (body_in_top_fourth or body_in_bottom_fourth) and wick_at_least_3x_body:
                pin_bars.append(i)  

        return pin_bars