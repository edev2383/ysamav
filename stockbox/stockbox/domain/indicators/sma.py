from stockbox.stockbox.domain.indicators.abs_indicator import AbstractIndicator


class SimpleMovingAverage(AbstractIndicator):
    name: str = "Simple Moving Average"
    abbr: str = "SMA"

    def _perform_calculations(self):
        # create a local copy that we'll do the calcs on
        self.df = self.df[::-1]
        cp_df = self.df.copy()
        # assign the calculations to the identifier
        cp_df[self.df_colkey] = self._calc_sma(cp_df)
        # for most of the indicators, we'll want to do our calculations
        # in chronological order, but we'll want to reverse them on
        # return because the .head() of our DataFrame is present day and
        # the .tail() is the beginning of the historical data
        return cp_df.iloc[::-1].fillna(0)[self.df_colkey]

    def _calc_sma(self, df):
        ci = self.column_identifier
        rg = int(self.args[0])
        return df.iloc[:, ci].rolling(window=rg).mean()
