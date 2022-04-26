from stockbox.stockbox.domain.setups.setup_list import SetupList
from stockbox.stockbox.domain.users.i_user import IUser


class BucketTickerProfile:

    """Contains the desired symbol to be scanned as well as all setups
    allowed for the given symbol. The TickerProfile is what is contained
    within the buckets, so at time of scan, the TickerProfile will
    regulate which setups are scanned for each symbol."""

    symbol: str
    user: IUser

    def __init__(self, symbol: str, user: IUser):
        self.symbol = symbol
        self.user = user
