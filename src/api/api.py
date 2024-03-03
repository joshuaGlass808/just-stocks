from flask import Flask, json

stocks = [{'MSFT': {'high': {'x': ['2024-03-01', '2024-02-23', '2024-02-16', '2024-02-09'], 'y': [415.87, 415.86, 420.74, 420.82]}, 'low': {'x': ['2024-03-01', '2024-02-23', '2024-02-16', '2024-02-09'], 'y': [403.85, 397.22, 403.39, 402.91]}, 'close': {'x': ['2024-03-01', '2024-02-23', '2024-02-16', '2024-02-09'], 'y': [415.5, 410.34, 404.06, 420.55]}}}]

api = Flask(__name__)

@api.route('/stocks', methods=['GET'])
def get_stocks():
  return json.dumps(stocks)

if __name__ == '__main__':
    api.run(debug=True, host='0.0.0.0', port=5000)