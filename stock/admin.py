from django.contrib import admin
from stock.models import Stock

# Register your models here.
class StockAdmin(admin.ModelAdmin):
    fields = ('stock_code','stock_name','stock_price','stock_lastPrice','stock_openprice','stock_maxprice','stock_minprice','stock_dealqty','stock_dealmoney')
    list_display = ('stock_code','stock_name','stock_price','stock_lastPrice','stock_openprice','stock_maxprice','stock_minprice','stock_dealqty','stock_dealmoney')

admin.site.register(Stock,StockAdmin)