import re
from stockbox.stockbox.common.helpers.enums import ETickerRequestFrequency
from stockbox.stockbox.common.results.result import ResultList
from . import PositionModel, IPosition, Ticker, Setup, EBucket
from .fakes.fake_setups import setup_01_simple_pattern_prime
import pandas as pd


def test_position_process_setup_01():
    # Since these tests are integrating with actual, live stock data, we
    # cannot guess what the results will be, instead we'll get the
    # target DataFrame from the ticker and extract the data ourselves
    # to mock the rule data with booleans and then compare the actual
    # results with our expected results from the concrete values
    setup = setup_01_simple_pattern_prime()
    model = _create_position_model("MSFT", setup, EBucket.eBase)
    position = IPosition(model)
    position.process()
    df = model.ticker.clone_for_setup(ETickerRequestFrequency.eDaily)
    # Get the actual values from the dataframe that represent the values
    # that should be returned by the evaluator in the rules
    close = get_value_from_df("Close", 0, df)
    close_1DA = get_value_from_df("Close", 1, df)
    sma_20 = get_value_from_df("SMA(20)", 0, df)
    sma_50 = get_value_from_df("SMA(50)", 0, df)
    # replicate the rule evaluation boolean value
    rule_one = close > close_1DA
    rule_two = sma_20 > sma_50
    # as of now, all rules are implied to be of an AND relationship
    # considering making the rules more complex and allowing ORs
    # expected will tell us if the rule should pass or not
    expected = rule_one and rule_two
    # the values found by the Evaluator are elevated and stashed in the
    # position resultlist, so we can perform a direct comparison
    result_resolution = confirm_expected_output(position.results)
    assert expected == result_resolution
    # Here is the tricky part: has_errors is the inverse of expected.
    # i.e., if expected is true, meaning that all the rules in the set
    # have passed, then has_errors is false. The opposite is true. The
    # has_errors method is not intended to be widely used as public
    # interface, but is left public for testing and resultlist reporting
    assert position.results.has_errors() != expected


def test_position_process_setup_02():
    setup = setup_01_simple_pattern_prime()
    model = _create_position_model("TSLA", setup, EBucket.eBase)
    position = IPosition(model)
    position.process()
    df = model.ticker.clone_for_setup(ETickerRequestFrequency.eDaily)
    # Get the actual values from the dataframe that represent the values
    # that should be returned by the evaluator in the rules
    close = get_value_from_df("Close", 0, df)
    close_1DA = get_value_from_df("Close", 1, df)
    sma_20 = get_value_from_df("SMA(20)", 0, df)
    sma_50 = get_value_from_df("SMA(50)", 0, df)
    # replicate the rule evaluation boolean value
    rule_one = close > close_1DA
    rule_two = sma_20 > sma_50
    # expected will tell us if the rule should pass or not
    expected = rule_one and rule_two
    # expected is the inverse of has_errors
    result_resolution = confirm_expected_output(position.results)
    assert expected == result_resolution
    assert position.results.has_errors() != expected


def _create_position_model(symbol, setup, bucket):
    return PositionModel(Ticker(symbol), setup, bucket)


def get_value_from_df(column: str, index: int, df: pd.DataFrame):
    return df.iloc[int(index)].at[column]


def confirm_expected_output(results: ResultList):
    """The values found in the Evaluator are elevated to the Rule
    and output in the Result via the RuleResultOutput model. This function
    will return false if any of the rules have failed, so we can use
    this to directly compare against the expected results. We could also
    pull the values from the result.output.values list and perform more
    comparisons, but for now that is overkill"""
    for result in results:
        if result.output.resolution == False:
            return False
    return True
