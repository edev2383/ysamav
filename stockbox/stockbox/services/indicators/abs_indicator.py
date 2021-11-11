from abc import ABC, abstractmethod
import pandas as pd
import numpy as np


class AbstractIndicator(ABC):
    """ returns a df series which can be added to the Ticker's df """
    
    """ longform name """
    name: str
    """ short name, part of the df_colkey """
    abbr: str
    """ dataframe column index """
    df_colkey: str
    """ additional args, i.e., range of indicator SMA(10) """
    args: list
    """ Column index to target for calculations """
    column_identifier: str
    """ the main dataframe on which the output series is run """
    df: pd.DataFrame
    """ the indicator results, usually a single column """
    output: pd.DataFrame

    def __init__(self, data: pd.DataFrame, args: list):
        self.column_identifier = self._column_index(data, ["Adj Close"])
        self.df = data
        self.args = args
        self.df_colkey = self._create_df_colkey()
        self.output = self._perform_calculations()

    @abstractmethod
    def _perform_calculations(self):
        pass

    def _column_index(self, data, query_cols):
        cols = data.columns.values
        sidx = np.argsort(cols)
        return sidx[np.searchsorted(cols, query_cols, sorter=sidx)]

    def _create_df_colkey(self):
        return f"{self.abbr}({','.join(self.args)})"