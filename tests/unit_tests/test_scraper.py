from . import Scraper, IScraperPayload
from .fakes.fake_scraper_parser import FakeScraperParser
from .fakes.fake_scraper_provider import FakeScraperProvider
from .fakes.fake_scaper_provider_in_params import FakeScraperProviderInParams


def test_scrapper_can_be_created():
    scraper = Scraper(None, None)
    assert scraper != None


def test_scraper_can_accept_fakes():
    scraper = __create_scraper_with_fakes()
    assert scraper != None
    assert scraper.parser != None
    assert scraper.provider != None


def test_scaper_scrape_method_returns_expected_value():
    scraper = __create_scraper_with_fakes()
    scraper.scrape()
    assert scraper.payload != None
    assert isinstance(scraper.payload, IScraperPayload)
    assert scraper.payload.output[0] == "abc123"


def __create_scraper_with_fakes():
    return Scraper(
        FakeScraperProvider(FakeScraperProviderInParams()), 
        FakeScraperParser())
