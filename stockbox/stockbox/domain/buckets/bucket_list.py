from stockbox.stockbox.common.helpers.enums import EBucket
from stockbox.stockbox.domain.buckets.bucket import Bucket
from ...common.base.ulist import Ulist


class BucketList(Ulist):
    def add_bucket(self, bucket: Bucket):
        self.append(bucket)

    def get(self, bucket: EBucket):
        for item in self:
            if item.bucket == bucket:
                return item
        return None

    def transition(self, symbol: str, old: EBucket, new: EBucket) -> Bucket:
        self._remove_stock_from(symbol, old)
        self._add_stock_to(symbol, new)

    def _add_stock_to(self, symbol: str, bucket: EBucket):
        found_bucket = self.get(bucket)
        if found_bucket == None:
            raise ValueError(f"Bucket not found: {bucket}")
        found_bucket.append(symbol)

    def _remove_stock_from(self, symbol: str, bucket: EBucket):
        found_bucket = self.get(bucket)
        if found_bucket == None:
            raise ValueError(f"Bucket not found: {bucket}")
        found_bucket.remove(symbol)
