import urllib
import demjson
import time
# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render

from stock.models import Stock

def home(request):
    string = "This is a websit about stock information!!!"
    return render(request,'Home.html',{'String':string})

def spiderAllStock():
    start_url = 'http://vip.stock.finance.sina.com.cn/quotes_service/api/json_v2.php/Market_Center.getHQNodeData?'
    json_array =[]
    for i in range(1,42):
        time.sleep(5)
        try:
            parm = {}
            parm['page'] = i
            parm['num'] = 80
            parm['node'] = 'hs_a'
            url_values = urllib.parse.urlencode(parm)
            full_url = start_url + url_values
            print(full_url)
            req = urllib.request.Request(full_url)
            req.add_header('User-Agent',
                           'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.101 Safari/537.36')
            response = urllib.request.urlopen(req)
            cont = response.read().decode('gbk')
            jsonobject = demjson.decode(cont)
            json_array.extend(jsonobject)
        except:
            print("Fail!")
    return json_array

def updatestock(request):
    stockjson = spiderAllStock()
    for o in stockjson:
        try:
            stock = Stock.objects.get(stock_code=o['code'])
            stock.stock_code = o['code']
            stock.stock_name = o['name']
            stock.stock_price = o['trade']
            stock.stock_openprice = o['open']
            stock.stock_minprice = o['low']
            stock.stock_maxprice = o['high']
            stock.stock_dealmoney=o['amount']
            stock.stock_dealqty = o['volume']
            stock.stock_lastPrice = o['settlement']
            stock.save()
        except Stock.DoesNotExist:
            stock = Stock()
            stock.stock_code = o['code']
            stock.stock_name = o['name']
            stock.stock_price = o['trade']
            stock.stock_openprice = o['open']
            stock.stock_minprice = o['low']
            stock.stock_maxprice = o['high']
            stock.stock_dealmoney = o['amount']
            stock.stock_dealqty = o['volume']
            stock.stock_lastPrice = o['settlement']
            stock.save()
    return HttpResponse("同步成功！！")
