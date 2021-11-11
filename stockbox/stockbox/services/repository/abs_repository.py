from abc import ABC, abstractmethod
from ..scraper.scraper import Scraper

class AbstractRepository(ABC):
    
    def _exec(self, scraper: Scraper):
        """ Currently ONLY scraping, but will also contain error 
        reporting """
        scraper.scrape()