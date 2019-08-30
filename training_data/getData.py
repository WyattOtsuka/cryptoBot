import requests
import json


#note that not all api will use this base
krakenBase = 'https://api.kraken.com'

recentTradeRes = requests.get(krakenBase + '/0/public/Trades',
    params = {
        'pair' : 'ETHUSD',
        'last' : 1517940026183120884
    }
)

trades = json.loads(recentTradeRes.content)['result']['XETHZUSD']


minTrade = 100000000
maxTrade = 0

for trade in trades:
    if minTrade > float(trade[0]):
        minTrade = float(trade[0])
        print("set minTrade to " + str(trade[0]))
    elif maxTrade < float(trade[0]):
        maxTrade = float(trade[0])
        print("set maxTrade to " + str(trade[0]))
print("Lowest Trade-----" + str(minTrade))
print("Highest Trade----" + str(maxTrade))