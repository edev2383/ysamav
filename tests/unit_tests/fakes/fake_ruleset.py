from stockbox.stockbox.domain.ticker.ticker import Ticker
from .fake_ticker import FakeTicker
from .. import RuleSet, Rule, EBucket


def fake_passing_ruleset_base_bucket():
    ruleset = RuleSet()
    # Close = 8, Open = 7
    r_one = Rule("Close > Open")
    # 2 days ago Close = 10, Open = 7
    r_two = Rule("2 days ago Close > Open")
    # 3 days ago Low = 9, 4 days ago High = 13
    r_tre = Rule("three days ago Low < 4 days ago High")
    ruleset.add_rule(r_one)
    ruleset.add_rule(r_two)
    ruleset.add_rule(r_tre)
    ruleset.set_bucket(EBucket.eBase)
    return ruleset


def fake_failing_ruleset_base_bucket_one_of_three_fail():
    ruleset = RuleSet()
    # Close = 8, Open = 7
    r_one = Rule("Close > Open")
    # 2 days ago Close = 10, Open = 7
    r_two = Rule("2 days ago Close > Open")
    # 3 days ago Low = 9, 4 days ago High = 13
    r_tre = Rule("three days ago Low > 4 days ago High")
    ruleset.add_rule(r_one)
    ruleset.add_rule(r_two)
    ruleset.add_rule(r_tre)
    ruleset.set_bucket(EBucket.eBase)
    return ruleset
