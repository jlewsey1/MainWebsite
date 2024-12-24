from flask import Flask, render_template
from ebaysdk.finding import Connection
from dotenv import load_dotenv
import os

load_dotenv()

api_key = os.getenv('API_KEY')
app = Flask(__name__)

@app.route('/')
def index():
    # Fetch the eBay price using your API logic
    api = Connection(appid=self.api_key, config_file=None)
    response = api.execute('findItemsAdvanced', {
        'keywords': 'PSA 10 Japanese Mega Rayquaza EX 095/081',
        'itemFilter': [
            {'name': 'MinPrice', 'value': 100},
            {'name': 'MaxPrice', 'value': 750},
            {'name': 'MaxEntries', 'value': 10}, # 10 max entries between 100-750
        ]
    })
    
    # Extract price from the response
    prices = [float(item.sellingStatus.currentPrice.value) for item in response.reply.searchResult.item]
    average = int(round(sum(prices)/len(prices)))

    # Pass the price to the HTML template
    return render_template('index.html', price=average)

if __name__ == '__main__':
    app.run(debug=True)
