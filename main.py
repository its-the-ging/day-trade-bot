from data_collector import create_ticker_obj, print_ticker_info, get_ticker_data, plot_high_low_of_period


company_ticker_dict = {
    'Google': 'GOOGL',
    'Apple': 'AAPL'
}

def main():
    google_ticker = create_ticker_obj(ticker_symbol=company_ticker_dict.get('Google'))
    plot_high_low_of_period(ticker_obj=google_ticker)
    return


if __name__ == '__main__':
    main()

