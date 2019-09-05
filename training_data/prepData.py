print("Starting...")
import datetime
startingTime = datetime.datetime.now()

import pandas as pd
import plotly.express as px

bigDf = pd.DataFrame()

data = pd.read_csv('data_10.csv')

for i in range(11,15):
    path = 'data_' + str(i) + '.csv'
    temp = pd.read_csv(path)
    data = data.append(temp, ignore_index = True)

print("Started")

rowList = []
currEpoch = int(data['time'][0])
sumPrices = 0
transCount = 0
print("Averaging...")
#averages prices within the same second
for idx, row in data.iterrows():
    rowTime = int(row['time'])
    if (rowTime == currEpoch): #still within the same second
        sumPrices += float(row['price'])
        transCount += 1
    else: #new time
        price = sumPrices / transCount
        dt = {}
        dt.update({'Price' : price, 'Time' : currEpoch})
        rowList.append(dt)
        currEpoch = rowTime
        sumPrices = float(row['price'])
        transCount = 1

avgedOut = pd.DataFrame(rowList) #DF with only one entry per second

print("Finished Averaging in " + str(datetime.datetime.now() - startingTime))


startingTime = datetime.datetime.now()
print("Filling...")
#fills in the gaps in the data
lastPrice = -1
lastTime = -1
rowListAvg = []
for idx, row in avgedOut.iterrows():

    currUnix = row['Time']
    currPrice = row['Price']
    if lastPrice != -1:   #Not the first loop

        if lastTime + 1 < currUnix:   #gap exists in the data

            #finds the linear slope between the two points
            slope = (currPrice - lastPrice) / (currUnix - lastTime)
            while currUnix > lastTime: #fills the gap and the current data point

                dt = {}
                lastTime += 1
                lastPrice += slope
                dt.update({"Price" : lastPrice, "Time" : lastTime})

                rowListAvg.append(dt)

        else: #no gap in the data

            dt = {}
            dt.update({"Price" : currPrice, "Time" : currUnix})
            rowListAvg.append(dt)

    else: #first loop

        dt = {}
        dt.update({"Price" : currPrice, "Time" : currUnix})
        rowListAvg.append(dt)



    lastPrice = row['Price']
    lastTime = row['Time']

filledDf = pd.DataFrame(rowListAvg)
print("Finished Filling in " + str(datetime.datetime.now() - startingTime))

filledDf.to_csv(path_or_buf = 'evenData.csv')

fig = px.line(filledDf, x = 'Time', y = 'Price', title='BTC Price over time')

fig.show()