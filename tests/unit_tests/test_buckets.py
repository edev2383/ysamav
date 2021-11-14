from . import Bucket, BaseBucket


def test_bucket_can_be_created():
    bucket = Bucket()
    assert bucket is not None


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
