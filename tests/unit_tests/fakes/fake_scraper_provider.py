from .. import AbstractScraperProvider


class FakeScraperProvider(AbstractScraperProvider):
    url: str = "FINVIZ"

    fake_html: str = '<html><head></head><body><div class="scrape_target">abc123</div><div class="scrape_target">abc123</div></body></html>'

    def _scrape_url(self):
        return self.fake_html

    