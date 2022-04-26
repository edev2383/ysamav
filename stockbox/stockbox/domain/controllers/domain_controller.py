from stockbox.stockbox.domain.actions.action_profile import ActionProfile
from stockbox.stockbox.domain.buckets.bucket_list import BucketList
from stockbox.stockbox.domain.setups.setup_list import SetupList
from stockbox.stockbox.domain.positions.position_model import PositionModel
from stockbox.stockbox.domain.positions.i_position import IPosition
from stockbox.stockbox.domain.actions.action_handler import ActionHandler
from stockbox.stockbox.domain.ticker.ticker import Ticker


class DomainController:
    """The domain controller is responsible for all API interfacing and
    scanning of the buckets/setups."""

    buckets: BucketList
    setups: SetupList

    # ? Does the DomainController need to have any knowledge of the
    # ? scanning interval? Or does it just scan what we give it? Leaning
    # ? toward the latter
    def __init__(self, buckets: BucketList, setups: SetupList):
        self.buckets = buckets
        self.setups = setups

    def scan(self):
        for bucket in self.buckets:
            # right now the stock in the buckets are just strings, but
            # they really should be a StockProfile, that will allow us
            # to maintain some state from setup run to run, and would
            # allow us to make some decisions as the stocks move from
            # bucket to bucket. i.e., a stock moves from one bucket to
            # another, but the second bucket setup ALSO triggers. Should
            # it actually react, or since it was just moved, do we ignore?
            for ticker_profile in bucket:
                for setup in ticker_profile.setups:
                    model = PositionModel(Ticker(ticker_profile), setup, bucket)
                    position = IPosition(model)
                    position.process()
                    if position.results.has_errors() == False:
                        ActionHandler(position, self).process()

    def buy(self, profile: ActionProfile):
        ...

    def sell(self, profile: ActionProfile):
        ...


# TODO - Need to add a reporting module. A way to raise all actions up to the
# TODO - top level and log it. Could be a text log for now
# TODO -
# TODO -
# TODO -
# TODO -
# TODO -
# TODO -
# TODO -
# TODO -
