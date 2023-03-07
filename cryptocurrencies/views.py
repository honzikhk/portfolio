from django.views.generic import ListView, TemplateView
from .models import CryptoCurrency

from cryptocurrencies.common.my_functions import extract_id


class CryptocurrenciesHomepageView(ListView):
    model = CryptoCurrency
    template_name = "cryptocurrencies/homepage.html"
    # paginate_by = 100  # pagination = more pages of content. didnt try yet

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        my_object_list = CryptoCurrency.objects.all()
        list_of_names = []
        for each in my_object_list:
            list_of_names.append(each.name)
        context["coins"] = extract_id(list_of_names)
        # context['now'] = timezone.now()
        return context






class HomepageView(TemplateView):   # this view maybe should be moved somewhere away, same the main_homepage.html
    template_name = "cryptocurrencies/main_homepage.html"