from django.views.generic import ListView
from .models import CryptoCurrency

from cryptocurrencies.common.my_functions import extract_id, find_price


class CryptocurrenciesHomepageView(ListView):
    model = CryptoCurrency
    template_name = "cryptocurrencies/crypto_homepage.html"
    # paginate_by = 100  # pagination = more pages of content. didnt try yet

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        my_object_list = CryptoCurrency.objects.all()
        list_my_object_list = CryptoCurrency.objects.values()

        list_of_names = []

        for each in my_object_list:         # create list of names. This list is used for extract id´s (need id for searching price later - best practise CMCAPI)
            list_of_names.append(each.name)
        context["coins_id"] = extract_id(list_of_names)     # dictionary of pairs name:id

        coins_total_balance = {}
        for each in list_my_object_list:
            name = each["name"].capitalize()
            price = find_price(context["coins_id"][name])
            balance = each["amount"] * price
            coins_total_balance[each["name"]] = round(balance, 2)       # for accurate balance maybe should not use round
        context["coins_balance"] = coins_total_balance

        total_crypto_balance = 0
        for key, value in context["coins_balance"].items():
            total_crypto_balance += value
        context["total_crypto_balance"] = total_crypto_balance
        return context
