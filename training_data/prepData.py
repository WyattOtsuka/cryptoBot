import pandas as pd
import datetime
data = pd.read_csv('test.csv')

currEpoch = datetime.datetime.strptime(data['dtime'][0][0:19], '%Y-%m-%d %H:%M:%S')
sumPrices = 0
transCount = 0

for row in data.iterrows():
    rowTime = datetime.datetime.strptime(row[1]['dtime'][0:19], '%Y-%m-%d %H:%M:%S')
    if (rowTime == currEpoch):
        sumPrices += float(row[1]['price'])
        transCount += 1
    else:
        

currEpoch = datetime.datetime.strptime(data['dtime'][0][0:19], '%Y-%m-%d %H:%M:%S')



print(currEpoch)
#for index in range(500000):
    