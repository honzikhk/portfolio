from django.views.generic import ListView, TemplateView
from .models import CryptoCurrency

from cryptocurrencies.common.my_functions import extract_id, find_prices


class CryptocurrenciesHomepageView(ListView):
    model = CryptoCurrency
    template_name = "cryptocurrencies/homepage.html"
    # paginate_by = 100  # pagination = more pages of content. didnt try yet

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        my_object_list = CryptoCurrency.objects.all()
        list_of_names = []
        for each in my_object_list:         # create list of names. This list is used for extract id´s (need id for searching price later - best practise CMCAPI)
            list_of_names.append(each.name)
        context["coins_id"] = extract_id(list_of_names)     # dictionary of pairs name:id
        context["coins_prices"] = find_prices(context["coins_id"])

        return context






class HomepageView(TemplateView):   # this view maybe should be moved somewhere away, same the main_homepage.html
    template_name = "cryptocurrencies/main_homepage.html"