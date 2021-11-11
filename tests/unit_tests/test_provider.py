from stockbox.stockbox.services.scraper.providers.yf_current_provider import YahooFinanceCurrentProvider
from stockbox.stockbox.services.scraper.providers.yf_current_provider_in_params import YahooFinanceCurrentProviderInParams


def test_provider_url_template_returns_correct_string():
    provider_in_params = YahooFinanceCurrentProviderInParams("MSFT")
    provider = YahooFinanceCurrentProvider(provider_in_params)
    url = provider._template_url()
    assert url == "https://finance.yahoo.com/quote/MSFT/history?p=MSFT"
    
