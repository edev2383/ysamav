from abc import ABC, abstractmethod
from lxml import html


class AbstractScraperParser(ABC):
    """ Each ScraperParser defines their own xpath_target and returns an
    IScraperPayload object model to the Scraper """
    xpath_target: any

    def parse(self, input):
        return self._parse_input(input)
    
    def _parse_input(self, input):
        tree = html.fromstring(input)
        return self._process_scraped_target(tree.xpath(self.xpath_target))
    
    @abstractmethod
    def _process_scraped_target(self, scraped_input):
        """ Return an IScraperPayload, specific to each ScraperParser """
        pass
