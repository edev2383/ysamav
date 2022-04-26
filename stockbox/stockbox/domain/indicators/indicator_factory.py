import pandas as pd
import re
from .sma import SimpleMovingAverage

indicators = {
            "sma": SimpleMovingAverage,
            # "slosto": SlowStochastic,
            # "slowsto": SlowStochastic,
            # "rsi": RelativeStrengthIndex,
            # "ema": ExponentialMovingAverage,
            # "slope": Slope,
        }

class IndicatorFactory:
    
    re_range = r"(.*)\(([0-9,]+)\)"
    df: pd.DataFrame
    tag: str
    agrs: list #(str)

    def create(self, df_colkey: str, df: pd.DataFrame):
        """ returns a data series """
        self._parse_colkey(df_colkey)
        return self._create(df.copy())

    def _create(self, df: pd.DataFrame):
        if self.tag in indicators.keys():
            func = indicators[self.tag]
            return func(df, self.args)
        raise ValueError(f"Requested indicator unknown [{self.tag}]")

    def _parse_colkey(self, key: str):
        found = re.match(self.re_range, key)
        if found:
            self.tag = found.group(1).strip().lower()
            self.args = found.group(2).strip().split(",")
        