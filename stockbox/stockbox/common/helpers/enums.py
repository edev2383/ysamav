from enum import Enum, IntEnum


class ETickerRequestFrequency(Enum):
    eDaily = "1d"
    eWeekly = "1wk"
    eMonthly = "1mo"


class ETickerRequestRange(IntEnum):
    # range of days
    eCustomRange = 0
    eOneWeek = 7
    eOneMonth = 30
    eThreeMonth = 90
    eSixMonths = 180
    eOneYear = 365
    eTwoYear = 730
    eFiveYear = 1825
    eTenYear = 3650


class ETickerRequestType(IntEnum):
    eHistory = 1


class EBucket(IntEnum):
    eBase = 0
    ePrime = 1
    eActive = 2
    eBrokenDown = 3
    eSold = 4
    eDefunct = 5


class EResult(IntEnum):
    eFail = 0
    eSuccess = 1
