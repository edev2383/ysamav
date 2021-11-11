from abc import ABC, abstractmethod
from stockbox.stockbox.services.base.model_base import ModelBase
from .i_scraper_provider_in_params import IScraperProviderInParams
import string


class AbstractScraperProvider(ABC):
    """ The ScraperProvider(s) perform the HTTP request and 
    returns the webpage content to be parsed """
    url: str
    in_params: IScraperProviderInParams
    output: str

    def __init__(self, in_params: IScraperProviderInParams):
        self.in_params = in_params

    def scrape(self):
        self.output = self._scrape_url()

    @abstractmethod
    def _scrape_url(self):
        """ Return the content of the target url 
        
        Note: I would like to make this a method of the base abstract 
        class, rather than an abstract method and push the handling of 
        the return response to a method that specifically handles the
        response content specific to each sub-class, but I am wanting to
        see how different types of ScraperProviders will be retrieving
        and utilizing their scraped content """
        pass

    def _template_url(self):
        template_url = string.Template(self.url)
        return template_url.safe_substitute(self.in_params.__dict__)
