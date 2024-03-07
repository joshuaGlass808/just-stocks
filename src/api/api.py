import sqlite3

from common_lib.db import stocks
from flask import Flask, json


api = Flask(__name__)


def organize_query_results(res):
    results = {}
    # 0:date, 1:stock, 2:high, 3:low, 4:close
    for record in res:
        if record[0] not in results:
            results[record[0]] = {}
        results[record[0]][record[1]] = {'high': record[2], 'low': record[3], 'close': record[4]}
    return results


@api.route('/stocks', methods=['GET'])
def get_stocks():
    stocks = organize_query_results(stocks.get_all())
    return json.dumps(stocks)


if __name__ == '__main__':
    api.run(debug=True, host='0.0.0.0', port=5000)
