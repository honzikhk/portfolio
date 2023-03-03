from django.views.generic import ListView
from .models import CryptoCurrency


class CryptocurrenciesHomepageView(ListView):
    model = CryptoCurrency
    template_name = "cryptocurrencies/homepage.html"


def get_price_per_coin(coin):
    return price