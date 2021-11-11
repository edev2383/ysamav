from . import DateRange, ETickerRequestRange


def test_date_range():
    r = DateRange(ETickerRequestRange.eFiveYear)
    assert r.range_str["start"] != None
    assert r.range_str["end"] != None
    assert r.range_int["start"] != None
    assert r.range_int["end"] != None
    assert r.range_str["start"] != r.range_str["end"]
    assert r.range_int["start"] != r.range_int["end"]
    assert r.range_str["start"] != r.range_int["start"]
    assert r.range_str["end"] != r.range_int["end"]
