from django.views.generic import ListView, TemplateView
from .models import CryptoCurrency


class CryptocurrenciesHomepageView(ListView):
    model = CryptoCurrency
    template_name = "cryptocurrencies/homepage.html"


def get_price_per_coin(coin):
    return price


class HomepageView(TemplateView):   # this view maybe should be moved somewhere away, same the main_homepage.html
    template_name = "cryptocurrencies/main_homepage.html"