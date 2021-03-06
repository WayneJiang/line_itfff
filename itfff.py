import requests
import datetime
import pandas
import numpy
import talib

#Line Notify
def Line(msg):   
    url = ('https://maker.ifttt.com/trigger/update/with/key/dRpC2gm9MCzrCHayYmTaq8?value1='+str(msg))
    r = requests.get(url)
    if r.text[:5] == 'Congr':  
        print('成功推送至 Line')
    return r.text

def GetPrice(symbol):
    try:
        price = requests.get('https://api.binance.com/api/v3/ticker/price', params={'symbol': symbol}).json()['price']
    except Exception as e:
        print ('Error! problem is {}'.format(e.args[0]))
    return float(price)

def GetKLine(symbol):
    try:
        json = requests.get('https://api3.binance.com/api/v3/klines',params={'symbol':symbol,'interval': '1m', 'limit': 60}).json()
        #print(json)
    except Exception as e:
        print ('Error! problem is {}'.format(e.args[0]))
    
    data_frame = pandas.DataFrame(columns= ['Open Time', 'Open', 'High', 'Low', 'Close', 'Volume', 'Close Time'])
    col_open_time, col_open, col_high, col_low, col_close, col_volume, col_close_time = [], [], [], [], [], [], []
    
    time_zone = datetime.timedelta(hours=8)
    
    for data in json:
        time = datetime.datetime.fromtimestamp(data[0]/1000)
        local_time = time + time_zone
        local_time.strftime("%Y/%m/%d %H:%M:%S")
        col_open_time.append(local_time)
        col_open.append(data[1])
        col_high.append(data[2])
        col_low.append(data[3])
        col_close.append(data[4])
        col_volume.append(data[5])
        time = datetime.datetime.fromtimestamp(data[6]/1000)
        local_time = time + time_zone
        local_time.strftime("%Y/%m/%d %H:%M:%S")
        col_close_time.append(local_time)
        
    data_frame['Open Time'] = col_open_time
    data_frame['Open'] = numpy.array(col_open).astype(numpy.float32)
    data_frame['High'] = numpy.array(col_high).astype(numpy.float32)
    data_frame['Low'] = numpy.array(col_low).astype(numpy.float32)
    data_frame['Close'] = numpy.array(col_close).astype(numpy.float32)
    data_frame['Volume'] = numpy.array(col_volume).astype(numpy.float32)
    data_frame['Close Time'] = col_close_time
    
    return data_frame
        
if __name__ == "__main__":
    #btc = GetPrice('BTCUSDT')
    #eth = GetPrice('ETHUSDT')
    #matic = GetPrice('MATICUSDT')
    #current_datetime = datetime.datetime.today()
    #time_zone = datetime.timedelta(hours=8)
    #local_datetime = current_datetime + time_zone
    #datetime_format = local_datetime.strftime("%Y/%m/%d %H:%M:%S")  
    #msg = 'Binance報價\n時間點 : ' + str(datetime_format) + '\n\nBTC即時價格 ： ' + str(btc) + ' 美元\nETH即時價格 ： ' + str(eth) + ' 美元\nMATIC即時價格 ： ' + str(matic) + ' 美元'
    #Line(msg)
    data_frame = GetKLine('BTCUSDT')
    macd, macdsignal, macdhist = talib.MACD(data_frame['Close'], fastperiod=12, slowperiod=26, signalperiod=9)
    print(macd)
    print(macdsignal)
    print(macdhist)
