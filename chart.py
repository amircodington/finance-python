# import yfinance as yf
import mplfinance as mpf
import pandas as pd
import numpy as np

from data import Data
from pivot import Pivot

class Chart:
    def __init__(self, data):
        self.data = data
        self.support = data.get_support()
        self.resistance = data.get_resistance()
        self.pin_bars = data.find_pin_bars()

    def pivot(self):
        target_pivot = Pivot(self.data.HIGHprev(), self.data.LOWprev(), self.data.CLOSEprev())
        rs_list = target_pivot.classic()
        rs1 = rs_list[0]
        rs2 = rs_list[1]
        rs3 = rs_list[2]
        # rs4 = rs_list[3]
        mpf.plot(self.data.symbol_data(), type='candle', show_nontrading=True, hlines=[rs1[0], rs1[1]])


    def pinbar(self):
        pin_bar_closes = pd.Series(np.nan, index=self.data.symbol_data().index)
        for i in self.pin_bars:
            pin_bar_closes.iloc[i] = self.data.symbol_data().iloc[i]['Close']
        scatter = mpf.make_addplot(pin_bar_closes, type='scatter', markersize=30, marker='^', color='r')
        mpf.plot(self.data.symbol_data(), type='candle', addplot=[scatter])
        
    def plot_support_resistance(self):
        # Calculate support and resistance levels
        support = self.support
        resistance = self.resistance
        data = self.data.symbol_data()

        # Add two lines for each support/resistance level to create a "box"
        lines = []
        for level in support:
            lines.append(mpf.make_addplot([level - 0.01]*len(data['Close']), color='green'))
            lines.append(mpf.make_addplot([level + 0.01]*len(data['Close']), color='green'))
        for level in resistance:
            lines.append(mpf.make_addplot([level - 0.01]*len(data['Close']), color='red'))
            lines.append(mpf.make_addplot([level + 0.01]*len(data['Close']), color='red'))

        # Plot data with support/resistance lines
        mpf.plot(data, type='candle', addplot=lines)
        
    def support_resistace(self):
        lines = []
        
        for _, value in self.support.items():
            lines.append(mpf.make_addplot([value]*len(self.data.data), panel=0, color='green', secondary_y=False))

        for _, value in self.resistance.items():
            lines.append(mpf.make_addplot([value]*len(self.data.data), panel=0, color='red', secondary_y=False))


        mpf.plot(self.data.symbol_data(), type='candle', addplot=lines)