from stockbox.stockbox.services.ticker.i_ticker import ITicker


class Ticker(ITicker):
    pass


# What does the ticker do? Ticker has a History, which is the df of past 
# values. Does the history also contain indicators? How are indicators 
# added?