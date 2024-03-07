import os
import requests
import sqlite3
import time

from common_lib.db import stocks

# TODO: List below should come from some other source..
S_LIST = ["AVGO", "META", "MSFT", "AMZN","GOOG","UNH","PANW","LLY","SNOW","MSTR","NFLX"]
API_TOKEN = os.getenv("ALPHAVANTAGE_API_TOKEN", "demo")


def capture_weekly_time_series_stock_data(stock_code):
    url = "https://www.alphavantage.co/query?function=TIME_SERIES_WEEKLY&symbol={}&apikey={}"
    r = requests.get(url.format(stock_code, API_TOKEN))
    data = r.json()

    for mkey, value in data["Meta Data"].items():
        print("{}: {}".format(mkey, value))
    
    print("Saving stock data...")
    stocks.write_weekly_time_series(stock_code, data)
    print(f"Done with {stock_code}!")


def main():
    while (True):
        for code in S_LIST:
            # Get weekly time series data and write to stock db
            capture_weekly_time_series_stock_data(code)
            # This sleep is because of the current rate limit for the API endpoint with demo account:)
            time.sleep(os.getenv('CAPTURE_API_SLEEP_TIME_SECONDS', 60))
        # Run every hour - by default
        time.sleep(os.getenv('CAPTURE_RUNTIME_ITERATION_SECONDS', 3600))
        # Check for any old data to clean up
        stocks.remove_old_weekly_series_data()


if __name__ == "__main__":
    main()
