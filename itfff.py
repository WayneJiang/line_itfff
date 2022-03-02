import requests
import datetime

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

if __name__ == "__main__":
    btc = GetPrice('BTCUSDT')
    eth = GetPrice('ETHUSDT')
    matic = GetPrice('MATICUSDT')
    now = datetime.datetime.now
    msg = 'Binance報價\n\n時間點 : ' + str(now) + '\nBTC即時價格 ： ' + str(btc) + ' 美元\nETH即時價格 ： ' + str(eth) + ' 美元\nMATIC即時價格 ： ' + str(matic) + ' 美元\n'
    Line(msg)
    
