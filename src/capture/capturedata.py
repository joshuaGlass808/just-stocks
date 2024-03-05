import os
import requests
import sqlite3
import time

# TODO: List below should come from some other source..
S_LIST = ["AVGO", "META"] # "MSFT", "AMZN","GOOG","UNH","PANW","LLY","SNOW","MSTR","NFLX"]
API_TOKEN = os.getenv("ALPHAVANTAGE_API_TOKEN", "demo")


def stock_data_to_db():
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
                    check_query = "SELECT id from stocks where stock = '{}' AND date = '{}';".format(code, date)
                    exists = db.execute(check_query).fetchall()
                    if len(exists) > 0:
                        pass # skip
                    insert_query = "INSERT INTO stocks (stock, date, close, high, low) VALUES(?, ?, ?, ?, ?);"
                    print(insert_query)
                    db.execute(insert_query, [code, date, weekly_data["4. close"], weekly_data["2. high"], weekly_data["3. low"]])
                i = i + 1
            time.sleep(os.getenv('CAPTURE_API_SLEEP_TIME_SECONDS', 60)) # this is because of the current rate limit :)


def main():
    while (True):
        stock_data_to_db()
        time.sleep(os.getenv('CAPTURE_RUNTIME_ITERATION_SECONDS', 3600)) # Run every hour.


if __name__ == "__main__":
    main()
