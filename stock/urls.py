from django.conf.urls import url

from stock.views import updatestock

urlpatterns = [
    # ex: /stock/
    url(r'^updatestock/$', updatestock, name='updatestock'),
]