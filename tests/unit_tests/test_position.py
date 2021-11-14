from tests.unit_tests.fakes.fake_ruleset import (
    fake_failing_ruleset_base_bucket_one_of_three_fail,
    fake_passing_ruleset_base_bucket,
)
from tests.unit_tests.fakes.fake_ticker import FakeTicker
from . import PositionModel, IPosition, Setup, EBucket


def test_position_can_be_create():
    model = PositionModel(FakeTicker, Setup(), EBucket.eBase)
    position = IPosition(model)
    assert position is not None


def test_position_returns_expected_results_PASSING():
    ruleset = fake_passing_ruleset_base_bucket()
    setup = Setup()
    setup.add_ruleset(ruleset)
    model = PositionModel(FakeTicker(), setup, EBucket.eBase)
    position = IPosition(model)
    position.process()
    # we expect no errors because the passing ruleset returns eSuccess
    assert position.results.has_errors() == False


def test_position_returns_expected_results_FAILING():
    ruleset = fake_failing_ruleset_base_bucket_one_of_three_fail()
    setup = Setup()
    setup.add_ruleset(ruleset)
    model = PositionModel(FakeTicker(), setup, EBucket.eBase)
    position = IPosition(model)
    position.process()
    # we expect one error
    assert position.results.has_errors() == True
    assert position.results.error_count() == 1
