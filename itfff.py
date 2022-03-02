import requests
import time

#Line Notify
def Line(msg):   
    url = ('https://maker.ifttt.com/trigger/update/with/key/dRpC2gm9MCzrCHayYmTaq8?value1='+str(msg))
    r = requests.get(url)
    if r.text[:5] == 'Congr':  
        print('成功推送 (' +str(msg)+') 至 Line')
    return r.text

def GetPrice(symbol):
    try:
        price = requests.get('https://api.binance.com/api/v3/ticker/price', params={'symbol': symbol}).json()['price']
    except Exception as e:
        print ('Error! problem is {}'.format(e.args[0]))
    return float(price)

if __name__ == "__main__":
    while True:
        price = GetPrice('BTCUSDT')
        Line('比特幣即時價格 ： ' + str(price) + '美元')
        price = GetPrice('ETHUSDT')
        Line('乙太幣即時價格 ： ' + str(price) + '美元')
        time.sleep(10)
