from stockbox.stockbox.common.helpers.enums import EResult
from stockbox.stockbox.domain.rules.rule import Rule
from . import RuleSet
from .fakes.fake_ticker import FakeTicker


def test_ruleset_can_be_created():
    t = FakeTicker()
    rs = RuleSet(t)
    assert rs is not None


def test_ruleset_expressions_handle_volume_values_01():
    t = FakeTicker()
    rs = RuleSet(t)
    assert rs is not None
    # 2DA Volume = 12000, Volume = 10000
    r_one = Rule("2 days ago Volume > Volume")
    # Volume = 10000, 1DA Volume = 11000
    r_two = Rule("Volume > One Day Ago Volume * 0.85")
    rs.add_rule(r_one)
    rs.add_rule(r_two)
    assert r_one.process().status == EResult.eSuccess
    assert r_two.process().status == EResult.eSuccess
    output = rs.process()
    # print(output)
    # for r in output:
    #     print(f"r.values: {r.output.values}")
    # RuleSet.process returns a ResultList
    assert output.has_errors() == False
    assert output.error_count() == 0


def test_ruleset_outputs_expected_result_01():
    t = FakeTicker()
    rs = RuleSet(t)
    assert rs is not None
    # Close = 8, Open = 7
    r_one = Rule("Close > Open")
    # 2 days ago Close = 10, Open = 7
    r_two = Rule("2 days ago Close > Open")
    # 3 days ago Low = 9, 4 days ago High = 13
    r_tre = Rule("three days ago Low < 4 days ago High")
    rs.add_rule(r_one)
    rs.add_rule(r_two)
    rs.add_rule(r_tre)
    assert r_one.process().status == EResult.eSuccess
    assert r_two.process().status == EResult.eSuccess
    assert r_tre.process().status == EResult.eSuccess
    output = rs.process()
    # RuleSet.process returns a ResultList
    assert output.has_errors() == False
    assert output.error_count() == 0


def test_ruleset_outputs_expected_result_02():
    t = FakeTicker()
    rs = RuleSet(t)
    assert rs is not None
    # Close = 8, Open = 7
    r_one = Rule("Close < Open")
    # 2 days ago Close = 10, Open = 7
    r_two = Rule("2 days ago Close > Open")
    # 3 days ago Low = 9, 4 days ago High = 13
    r_tre = Rule("three days ago Low < 4 days ago High")
    rs.add_rule(r_one)
    rs.add_rule(r_two)
    rs.add_rule(r_tre)
    assert r_one.process().status == EResult.eFail
    assert r_two.process().status == EResult.eSuccess
    assert r_tre.process().status == EResult.eSuccess
    output = rs.process()
    # RuleSet.process returns a ResultList
    assert output.has_errors() == True
    assert output.error_count() == 1


def test_ruleset_outputs_expected_result_03():
    t = FakeTicker()
    rs = RuleSet(t)
    assert rs is not None
    # Close = 8, Open = 7
    r_one = Rule("Close > Open")
    # 2 days ago Close = 10, Open = 7
    r_two = Rule("2 days ago Close < Open")
    # 3 days ago Low = 9, 4 days ago High = 13
    r_tre = Rule("three days ago Low < 4 days ago High")
    rs.add_rule(r_one)
    rs.add_rule(r_two)
    rs.add_rule(r_tre)
    assert r_one.process().status == EResult.eSuccess
    assert r_two.process().status == EResult.eFail
    assert r_tre.process().status == EResult.eSuccess
    output = rs.process()
    # RuleSet.process returns a ResultList
    assert output.has_errors() == True
    assert output.error_count() == 1


def test_ruleset_outputs_expected_result_04():
    t = FakeTicker()
    rs = RuleSet(t)
    assert rs is not None
    # Close = 8, Open = 7
    r_one = Rule("Close > Open")
    # 2 days ago Close = 10, Open = 7
    r_two = Rule("2 days ago Close > Open")
    # 3 days ago Low = 9, 4 days ago High = 13
    r_tre = Rule("three days ago Low > 4 days ago High")
    rs.add_rule(r_one)
    rs.add_rule(r_two)
    rs.add_rule(r_tre)
    assert r_one.process().status == EResult.eSuccess
    assert r_two.process().status == EResult.eSuccess
    assert r_tre.process().status == EResult.eFail
    output = rs.process()
    # RuleSet.process returns a ResultList
    assert output.has_errors() == True
    assert output.error_count() == 1


def test_ruleset_outputs_expected_result_05():
    t = FakeTicker()
    rs = RuleSet(t)
    assert rs is not None
    # Close = 8, Open = 7
    r_one = Rule("Close < Open")
    # 2 days ago Close = 10, Open = 7
    r_two = Rule("2 days ago Close < Open")
    # 3 days ago Low = 9, 4 days ago High = 13
    r_tre = Rule("three days ago Low > 4 days ago High")
    rs.add_rule(r_one)
    rs.add_rule(r_two)
    rs.add_rule(r_tre)
    assert r_one.process().status == EResult.eFail
    assert r_two.process().status == EResult.eFail
    assert r_tre.process().status == EResult.eFail
    output = rs.process()
    # RuleSet.process returns a ResultList
    assert output.has_errors() == True
    assert output.error_count() == 3
