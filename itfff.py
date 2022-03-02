import requests
import time

#Line Notify
def Line(msg):   
    url = ('https://maker.ifttt.com/trigger/事件名稱/with/'+
          'key/金鑰' +
          '?value1='+str(msg))
    r = requests.get(url)      
    if r.text[:5] == 'Congr':  
        print('成功推送 (' +str(msg)+') 至 Line')
    return r.text

def GetPrice():
    try:
        price = requests.get('https://api.binance.com/api/v3/ticker/price', params={'symbol': symbol}).json()['price']
    except Exception as e:
        print ('Error! problem is {}'.format(e.args[0]))
    return float(price)

if __name__ == "__main__":
    while True:
        price = GetPrice(url, coin)
        Line(msg)
        time.sleep(10)
