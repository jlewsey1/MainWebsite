from flask import Flask
import datetime
from ebaysdk.exception import ConnectionError
from ebaysdk.finding import Connection
from dotenv import load_dotenv
import os

app = Flask(__name__)

@app.route('/', methods = ["GET"])

def home():
    load_dotenv()
    api_key = os.getenv('API_KEY')

    try: 
        api = Connection(appid=api_key, config_file=None)
        response = api.execute('findItemsAdvanced', {
            'keywords': 'PSA 10 Japanese Mega Rayquaza EX 095/081',
            'itemFilter': [
                {'name': 'MinPrice', 'value': 100},
                {'name': 'MaxPrice', 'value': 750},
                {'name': 'MaxEntries', 'value': 10}, # 10 max entries between 100-750
            ]
        })
        prices = [float(item.sellingStatus.currentPrice.value) for item in response.reply.searchResult.item]
        average = int(round(sum(prices)/len(prices)))

    except ConnectionError as e:
           print(e)
           print(e.response.dict())

    return f"<h1>Average price is {average}</h1>"

if __name__ == '__main__':
    app.run()   

# python3 -m venv tester
# source tester/bin/activate
# run these to create virtual environment