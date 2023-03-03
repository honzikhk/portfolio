from django.http import HttpResponse
from django.views.generic import ListView
from .models import CryptoCurrency


class CryptocurrenciesHomepageView(ListView):
    template_name = "cryptocurrencies/homepage.html"

    def get_queryset(self):
        return CryptoCurrency.objects.all()     # později přidat .filter(user=self.request.user)

    # def get_context_data(self, *args, **kwargs):
    #     context = super(CryptocurrenciesHomepageView, self).get_context_data(*args, **kwargs)
    #     extra_content = {

    #     }
    #     context.update(extra_content)
    #     return context
