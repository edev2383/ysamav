from . import Setup, RuleSet, EBucket
from .fakes.fake_ticker import FakeTicker
from .fakes.fake_ruleset import (
    fake_failing_ruleset_base_bucket_one_of_three_fail,
    fake_passing_ruleset_base_bucket,
)


def test_setup_can_be_created():
    setup = Setup()
    assert setup is not None


def test_setup_default_has_empty_ruleset_and_none_ticker():
    setup = Setup()
    assert setup.ticker is None
    assert len(setup.rulesets) == 0


def test_setup_can_recieve_rulesets():
    setup = Setup()
    ruleset_01 = RuleSet()
    ruleset_02 = RuleSet()
    setup.add_ruleset(ruleset_01)
    assert len(setup.rulesets) == 1
    # Ulist class does not allow duplicate entries
    setup.add_ruleset(ruleset_01)
    assert len(setup.rulesets) == 1
    setup.add_ruleset(ruleset_02)
    assert len(setup.rulesets) == 2


def test_setup_can_retrieve_rulesets_by_bucket_value():
    setup = Setup(FakeTicker())
    ruleset = RuleSet()
    ruleset.set_bucket(EBucket.eBase)
    setup.add_ruleset(ruleset)
    found_ruleset = setup.find_ruleset(EBucket.eBase)
    assert ruleset == found_ruleset
    assert found_ruleset.ticker is not None


def test_setup_returns_correct_passing_results_with_provided_fake_ticker():
    setup = Setup(FakeTicker())
    passing_ruleset = fake_passing_ruleset_base_bucket()
    setup.add_ruleset(passing_ruleset)
    result_list = setup.process(EBucket.eBase)
    assert result_list.has_errors() == False


def test_setup_returns_correct_failing_results_with_provided_fake_ticker():
    setup = Setup(FakeTicker())
    passing_ruleset = fake_failing_ruleset_base_bucket_one_of_three_fail()
    setup.add_ruleset(passing_ruleset)
    result_list = setup.process(EBucket.eBase)
    assert result_list.has_errors() == True
    assert result_list.error_count() == 1
