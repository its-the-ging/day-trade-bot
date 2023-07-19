"""
Project: day_trade_bot
File: data_collector.py
Authors: Quinn Graehling
Created On: 7/18/2023
Description: Scripts for collecting historical stock data using yfinance
"""

from yfinance import Ticker
import matplotlib.pyplot as plt

def create_ticker_obj(ticker_symbol: str):
    """
    Create a yfinance Ticker object
    :param ticker_symbol: The string associated with the stock Ticker
    :return: Ticker object
    """

    return Ticker(ticker_symbol)

def print_ticker_info(ticker_obj: Ticker):
    """
    Get the info of a Ticker object
    :param ticker_obj: yfinance Ticker object
    :return:
    """

    print(ticker_obj.get_info())
    return

def get_ticker_data(ticker_obj: Ticker, period: str = '1y', interval: str = '5d'):
    """
    Get the data of a stock using the Ticker object
    :param ticker_obj: The ticker object to pull data for
    :param period: The period of from past that you wish to gather
    :param interval: The interval between prices
    :return: The Ticker data for the given period and interval in the format of a pd dataframe
    """

    accepted_periods = ['1d', '5d', '1mo', '3mo', '6mo', '1y', '2y', '5y', '10y', 'ytd', 'max']
    accepted_intervals = ['1m', '2m', '5m', '15m', '30m', '60m', '90m', '1h', '1d', '5d', '1wk', '1mo', '3mo']

    assert period in accepted_periods, f'Period must be one of {accepted_periods}'
    assert interval in accepted_intervals, f'Period must be one of {accepted_intervals}'

    return ticker_obj.history(period=period, interval=interval)


def plot_high_low_of_period(ticker_obj: Ticker, period: str = '1y', interval: str = '1h'):
    """
    Plot the High and Low value of a stock over a given period
    :param ticker_obj: The ticker of the stock to plot
    :param period: The period of time to plot
    :param interval: The interval of time to plot
    :return:
    """

    ticker_df = get_ticker_data(ticker_obj=ticker_obj, period=period, interval=interval)
    highs = ticker_df['High']
    lows = ticker_df['Low']
    plt.plot(lows)
    plt.plot(highs)
    plt.show()
    return

