from django.urls import path
from .views import CryptocurrenciesHomepageView


urlpatterns = [
    path("", CryptocurrenciesHomepageView.as_view(), name="crypto_homepage"),
]