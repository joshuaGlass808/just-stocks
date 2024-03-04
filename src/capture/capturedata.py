import os
import requests
import sqlite3
import time

# TODO: List below should come from some other source..
S_LIST = ["AVGO"] # "MSFT", "AMZN","GOOG","UNH","PANW","LLY","SNOW","MSTR","NFLX"]
API_TOKEN = os.environ['ALPHAVANTAGE_API_TOKEN']


def gather_stock_data():
    # replace the "demo" apikey below with your own key from https://www.alphavantage.co/support/#api-key
    url = "https://www.alphavantage.co/query?function=TIME_SERIES_WEEKLY&symbol={}&apikey={}"
    results = {}
    with sqlite3.connect("/db/stocks.db") as conn:
        db = conn.cursor()

        for code in S_LIST:
            r = requests.get(url.format(code, API_TOKEN))
            data = r.json()

            for mkey, value in data["Meta Data"].items():
                print("{}: {}".format(mkey, value))

            i = 0
            for date, weekly_data in data["Weekly Time Series"].items():
                if i < 10:
                    q = "INSERT INTO stocks (stock, date, close, high, low) VALUES(?, ?, ?, ?, ?);"
                    print(q)
                    db.execute(q, [code, date, weekly_data["4. close"], weekly_data["2. high"], weekly_data["3. low"]])
                i = i + 1


def main():
    while (True):
        gather_stock_data()
        time.sleep(3600) # Run every hour.


if __name__ == "__main__":
    main()
