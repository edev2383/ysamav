import pandas as pd


class DataFrameEvaluator:
    """Created to wrap all logic around getting index and columns"""

    def evaluate(self, df: pd.DataFrame, index: int, column: str):
        val = df.iloc[int(index)].at[column]
        return val
