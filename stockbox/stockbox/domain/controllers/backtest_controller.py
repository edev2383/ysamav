from stockbox.stockbox.domain.buckets.bucket_list import BucketList
from stockbox.stockbox.domain.setups.setup_list import SetupList


class BacktestController():
    setups: SetupList
    bucket: BucketList

    def __init__(self, setups: SetupList, buckets: BucketList):
        self.setups = setups
        self.buckets = buckets