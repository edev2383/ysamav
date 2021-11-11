from . import Ticker

def test_ticker_can_be_created() :
    ticker = Ticker("MSFT")
    assert ticker != None