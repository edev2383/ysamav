from stockbox.stockbox.services.scraper.payload.yf_history_payload import YahooFinanceHistoryPayload
from .abs_scraper_parser import AbstractScraperParser
import pandas as pd
import io


class YahooFinanceHistoryParser(AbstractScraperParser):
    xpath_target = ''

    def _parse_input(self, input):
        """ There is no xpath, since this history is a csv download, so 
        we short-circuit the process_scraped_target """
        output = YahooFinanceHistoryPayload()
        scrape = pd.read_csv(io.StringIO(input))
        output.dataframe = scrape[::-1]
        return output

    def _process_scraped_target(self, scraped_input):
        """ unnecessary for this parser """
        pass