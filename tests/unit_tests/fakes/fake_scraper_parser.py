from .. import AbstractScraperParser
from .. import IScraperPayload
from lxml import html


class FakeScraperParser(AbstractScraperParser):
    xpath_target = '//div[@class="scrape_target"]/text()'

    def _process_scraped_target(self, scraped_input):
        payload = IScraperPayload()
        payload.output = scraped_input
        return payload
