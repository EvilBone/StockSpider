from django.conf.urls import url

from stock.views import updatestock

urlpatterns = [
    # ex: /polls/
    url(r'^$', updatestock, name='updatestock'),
]