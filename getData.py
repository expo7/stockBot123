import csv
from binance.client import Client
import pandas as pd
KEY ='Ju1K3tridhvKlaIzKBSKYyXTK8RlyQMyQ6p0oc5zoYIE0ULk661RukTXbqw0kXJn'
SECRET='Okgj48OQSvXQeHhqiqRSd8C08g4HjmN6Jt5JQnFg2vTjgwf72n8HqBTavRZnbmMy'
client = Client(KEY, SECRET)
candlesticks = client.get_historical_klines("BTCUSDT", Client.KLINE_INTERVAL_1DAY, "1 Jan, 2020", "12 Feb, 2020")
print(candlesticks)

time=[]
open=[]
high=[]
low=[]
close=[]
cols=['time', 'open', 'high', 'low','close']
for c in candlesticks:
  time.append(c[0]/1000)
  open.append(c[1])
  high.append(c[2])
  low.append(c[3])
  close.append(c[4])
data_list=[time,open,high,low,close]
df=pd.DataFrame(columns=cols)
df.time=time
df.open=open
df.low=low 
df.high=high 
df.close=close
df.to_csv('data.csv',index=False)
