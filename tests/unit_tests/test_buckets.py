from stockbox.stockbox.common.helpers.enums import EBucket
from . import Bucket, BaseBucket, BucketList

# ======================================================================
#
# ======================================================================


def test_bucketlist_can_be_create():
    bucketlist = BucketList()
    assert bucketlist is not None


def test_bucket_can_be_created():
    bucket = Bucket()
    assert bucket is not None


def test_new_bucketlist_can_have_length_and_is_empty():
    bucketlist = BucketList()
    assert len(bucketlist) == 0


def test_new_bucket_can_have_length_and_is_empty():
    bucket = Bucket()
    assert len(bucket) == 0


def test_bucketlist_can_accept_buckets():
    bucketlist = BucketList()
    basebucket = BaseBucket()
    bucketlist.append(basebucket)
    assert len(bucketlist) == 1


def test_bucket_can_accept_values():
    bucket = Bucket()
    assert len(bucket) == 0
    bucket.append(1)
    assert len(bucket) == 1
    bucket.append(2)
    assert len(bucket) == 2
    bucket.append(3)
    assert len(bucket) == 3


def test_bucketlist_can_retrieve_bucket_by_enum():
    bucketlist = BucketList()
    basebucket = BaseBucket()
    bucketlist.append(basebucket)
    found = bucketlist.get(EBucket.eBase)
    assert found is not None
    assert isinstance(found, BaseBucket)


def test_bucket_next_method_works_as_expected():
    bucket = Bucket()
    bucket.append(1)
    bucket.append(2)
    bucket.append(3)
    bucket.append(4)
    assert bucket.next() == 1
    assert bucket.next() == 2
    assert bucket.next() == 3
    assert bucket.next() == 4
    assert bucket.next() == None
    bucket.reset_pointer()
    assert bucket.next() == 1


def test_bucket_of_stock_strings():
    stocks = ["MSFT", "TSLA", "AMD"]
    base_bucket = BaseBucket()
    base_bucket.extend(stocks)
    assert base_bucket.next() == "MSFT"
    assert base_bucket.next() == "TSLA"
    assert base_bucket.next() == "AMD"
    assert base_bucket.next() == None
    base_bucket.reset_pointer()
    assert base_bucket.next() == "MSFT"
