import requests
import os

#import matplotlib.pyplot as plt

S_LIST = ["MSFT", "AVGO", "AMZN","GOOG","UNH","PANW","LLY","SNOW","MSTR","NFLX"]

key = os.environ['ALPHAVANTAGE_API_TOKEN']

# replace the "demo" apikey below with your own key from https://www.alphavantage.co/support/#api-key
url = "https://www.alphavantage.co/query?function=TIME_SERIES_WEEKLY&symbol={}&apikey={}"
results = {}

for code in S_LIST:
    r = requests.get(url.format(code, key))
    data = r.json()

    for mkey, value in data["Meta Data"].items():
        print("{}: {}".format(mkey, value))
    
    results[code] = {}
    high_x = []
    high_y = []

    close_x = []
    close_y = []

    low_x = []
    low_y = []
    i = 0
    for date, weekly_data in data["Weekly Time Series"].items():
        if i < 4:
            close_x.append(date)
            close_y.append(float(weekly_data["4. close"]))
            high_x.append(date)
            high_y.append(float(weekly_data["2. high"])) 
            low_x.append(date)
            low_y.append(float(weekly_data["3. low"]))
        i = i + 1

    results[code]["high"] = {"x": high_x, "y": high_y}
    results[code]["low"] = {"x": low_x, "y": low_y}
    results[code]["close"] = {"x": close_x, "y": close_y}


#plt.plot(high_x, high_y, marker='v', color='r')
#plt.plot(close_x, close_y, color='g', marker='*')
#plt.plot(low_x, low_y, marker='^')
#plt.xlabel("Date")
#plt.ylabel("Price High/Low")
#plt.title("Stock Chart")
#plt.show()

print(results)
