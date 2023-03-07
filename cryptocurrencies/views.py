from django.views.generic import ListView, TemplateView
from .models import CryptoCurrency


class CryptocurrenciesHomepageView(ListView):
    model = CryptoCurrency
    template_name = "cryptocurrencies/homepage.html"
    # paginate_by = 100  # pagination = more pages of content. didnt try yet

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context = funkce_co_vraci_dict_s_cenami
        # context['now'] = timezone.now()
        return context






class HomepageView(TemplateView):   # this view maybe should be moved somewhere away, same the main_homepage.html
    template_name = "cryptocurrencies/main_homepage.html"