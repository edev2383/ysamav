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
    # This is the first watchlist to which a stock symbol can be added.
    # Any stocks in this base WL will be checked against the appropriate
    # base RuleSets for each available Setup
    eBase = 0
    # Primed stocks have triggered a RuleSet and have been moved from
    # the base WL and will now be checked against the prime ruleset for
    # the same setup
    ePrime = 1
    # When a prime stock triggers a RuleSet, a "Position" is opened.
    # That means a stock is purchased
    eActivePosition = 2
    # The active position has entered a state where a sale might be
    # imminent
    ePositionExitPrime = 3
    # The stock is sold and moved to this watchlist
    eSold = 4
    # The stock is no longer in a state that is being actively tracked
    eBrokenDown = 5
    eRemoved = 6


class EResult(IntEnum):
    eFail = 0
    eSuccess = 1


class EBucketScanFrequency(IntEnum):
    eDailyOpen = 0
    eDailyClose = 1
    eHourly = 2
    eQuarterHourly = 3
    eWeekly = 4
    eMonthly = 5
    eOpenAndMidDay = 6
    eOpenAndQuarterPriorToClose = 7
    eMidDayAndClose = 8
    eMidDayAndQuarterPriorToClose = 9
    eOpenMidDayAndQuarterPriorToClose = 10
