from stockbox.stockbox.common.helpers.enums import EBucket
from ...common.base.ulist import Ulist


class Bucket(Ulist):
    pointer: int
    bucket: EBucket

    def __init__(self):
        self.pointer = 0
        Ulist.__init__(self)

    def next(self):
        if self.pointer == len(self):
            return None
        _ret = self[self.pointer]
        self._increment_pointer()
        return _ret

    def _increment_pointer(self):
        if self.pointer < len(self):
            self.pointer = self.pointer + 1

    def reset_pointer(self):
        self.pointer = 0


class BaseBucket(Bucket):
    bucket: EBucket = EBucket.eBase


class PrimeBucket(Bucket):
    bucket: EBucket = EBucket.ePrime


class ActivePositionBucket(Bucket):
    bucket: EBucket = EBucket.eActivePosition


class PositionBreakDownBucket(Bucket):
    bucket: EBucket = EBucket.ePositionExitPrime


class SoldBucket(Bucket):
    bucket: EBucket = EBucket.eSold


class BreakDownBucket(Bucket):
    bucket: EBucket = EBucket.eBrokenDown


class RemovedBucket(Bucket):
    bucket: EBucket = EBucket.eRemoved
