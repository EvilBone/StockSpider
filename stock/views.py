import urllib
import demjson
# Create your views here.
from django.http import HttpResponse

from stock.models import Stock

def spiderAllStock():
    start_url = 'http://vip.stock.finance.sina.com.cn/quotes_service/api/json_v2.php/Market_Center.getHQNodeData?'
    json_array =[]
    for i in range(1,16):
        parm = {}
        parm['page'] = i
        parm['num'] = 80
        parm['node'] = 'sz_a'
        url_values = urllib.parse.urlencode(parm)
        full_url = start_url + url_values
        response = urllib.request.urlopen(full_url)
        cont = response.read().decode('gbk')
        jsonobject = demjson.decode(cont)
        json_array.extend(jsonobject)
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
