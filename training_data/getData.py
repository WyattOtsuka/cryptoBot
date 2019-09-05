import requests
import json
import krakenex
from pykrakenapi import KrakenAPI as krakenapi
import pandas as pd
import datetime as dt
import time


api = krakenex.API()
k = krakenapi(api)

#original start 1496275199004099581
#last call: 1567211557033327104
#last pcount: 934
#fcount: 32


df = k.get_recent_trades('XXBTZUSD', since = 1567211557033327104)
trades = df[0]
trades = trades.reset_index()

last = df[1]
trades = trades.iloc[::-1]

pullcount = 934
headers = pullcount == 0
filecount = 29

fpath = ('data_' + str(filecount) + '.csv')

with open(fpath, 'a') as f:
    trades.to_csv(f, index = False, header = headers)

print(str(last) + " with a pcount of " + str(pullcount) + " and an fcount of " + str(filecount))


pullcount += 2

#1567206320579699960

while last < 1567206320579699960:
    time.sleep(5.99)
    df = k.get_recent_trades('XXBTZUSD', since = last)
    trades = df[0]  
    trades = trades.reset_index()
    last = df[1]

    trades = trades.iloc[::-1]

    headers = pullcount == 0

    with open(fpath, 'a') as f:
        trades.to_csv(f, header = headers, index = False)

    print(str(last) + " with a pcount of " + str(pullcount) + " and an fcount of " + str(filecount))

    pullcount += 2
    if pullcount > 998:
        pullcount = 0
        filecount += 1
        fpath = 'data_' + str(filecount) + '.csv'


'''
#note that not all api will use this base
krakenBase = 'https://api.kraken.com'

recentTradeRes = requests.get(krakenBase + '/0/public/Trades',
    params = {
        'pair' : 'XXBTZUSD',
        'last' : 1517940026183120884
    }
)

trades = json.loads(recentTradeRes.content)


minTrade = 100000000
maxTrade = 0

print(trades)

for trade in trades:
    if minTrade > float(trade[0]):
        minTrade = float(trade[0])
    elif maxTrade < float(trade[0]):
        maxTrade = float(trade[0])
        
print("Lowest Trade-----" + str(minTrade))
print("Highest Trade----" + str(maxTrade))
'''
