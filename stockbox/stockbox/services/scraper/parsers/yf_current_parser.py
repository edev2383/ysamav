from stockbox.stockbox.services.scraper.parsers.abs_scraper_parser import AbstractScraperParser
from stockbox.stockbox.services.scraper.payload.yf_current_payload import YahooFinanceCurrentPayload


class YahooFinanceCurrentParser(AbstractScraperParser):
    xpath_target = '//table[@data-test="historical-prices"]//tbody//tr[1]//td//span//text()'
    
    def _process_scraped_target(self, scraped_input):
        output = YahooFinanceCurrentPayload()
        output.date = str(scraped_input[0].replace(",", ""))
        output.open = float(scraped_input[1].replace(",", ""))
        output.high = float(scraped_input[2].replace(",", ""))
        output.low = float(scraped_input[3].replace(",", ""))
        output.close = float(scraped_input[4].replace(",", ""))
        output.adjclose = float(scraped_input[5].replace(",", ""))
        output.volume = int(scraped_input[6].replace(",", ""))
        return output
