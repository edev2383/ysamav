from .enums import ETickerRequestRange
import datetime
from datetime import datetime as dt


class DateRange:
    """
    Retrieve the start and end of a given range in both datetime and timestamp
    format
    """

    range_str: dict = {}
    range_int: dict = {}
    range: ETickerRequestRange

    eodHour: int = 18
    timezone_offset: int = 4

    def __init__(self, range: ETickerRequestRange):
        self._set_range(range)

    def _set_range(self, range: ETickerRequestRange):
        self._set_end()
        self._set_start(range)

    def _set_end(self):
        today = datetime.date.today()
        today_time = datetime.time(self.timezone_offset + self.eodHour, 0)
        self.range_str["end"] = dt.combine(today, today_time)
        self.range_int["end"] = int(dt.timestamp(self.range_str["end"]))

    def _set_start(self, range: ETickerRequestRange):
        offset = 3600 * 24 * int(range)
        offset_eod = 3600 * self.eodHour
        self.range_int["start"] = self.range_int["end"] - offset - offset_eod
        self.range_str["start"] = dt.fromtimestamp(self.range_int["start"])
