from django.db import models

# Create your models here.
class Stock(models.Model):
    stock_code = models.CharField(max_length=10,verbose_name="股票代码")
    stock_name = models.CharField(max_length=20,verbose_name="股票名称")
    stock_price = models.FloatField(max_length=6,verbose_name="当前价格",default=0)
    stock_lastPrice = models.FloatField(max_length=6,verbose_name="昨收",default=0)
    stock_openprice = models.FloatField(max_length=6,verbose_name="今开",default=0)
    stock_maxprice = models.FloatField(max_length=6,verbose_name="最高",default=0)
    stock_minprice = models.FloatField(max_length=6,verbose_name="最低",default=0)
    stock_dealqty = models.BigIntegerField(verbose_name="成交量/手",default=0)
    stock_dealmoney = models.BigIntegerField(verbose_name="成交额/万",default=0)