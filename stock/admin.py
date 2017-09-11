from django.contrib import admin
from stock.models import Stock

# Register your models here.
class StockAdmin(admin.ModelAdmin):
    fields = ('stock_code','stock_name','stock_price','stock_lastPrice','stock_openprice','stock_maxprice','stock_minprice','stock_dealqty','stock_dealmoney')
    list_display = ('stock_code','stock_name','stock_price','stock_lastPrice','stock_openprice','stock_maxprice','stock_minprice','stock_dealqty','stock_dealmoney')
    # list_filter = ('stock_price',)
    search_fields = ('stock_code','stock_name')
    # list_per_page设置每页显示多少条记录，默认是100条
    list_per_page = 10
    #list_editable = ('stock_price', 'stock_name')

admin.site.register(Stock,StockAdmin)