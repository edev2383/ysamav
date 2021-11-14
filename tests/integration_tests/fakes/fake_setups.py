from stockbox.stockbox.common.helpers.enums import EBucket
from stockbox.stockbox.domain.rules.ruleset import RuleSet
from stockbox.stockbox.domain.setups.setup import Setup
from .. import Rule


def setup_01_simple_pattern_prime():
    """This is a simple priming pattern for testing. Today closed higher
    than yesterday and the Simple Moving Average (20) is higher than the
    (50)
    """
    ruleone = Rule("Close > One Day Ago Close")
    ruletwo = Rule("SMA(20) > SMA(50)")
    #
    rule_set = RuleSet()
    rule_set.bucket = EBucket.eBase
    #
    rule_set.add_rule(ruleone)
    rule_set.add_rule(ruletwo)
    #
    setup = Setup()
    setup.add_ruleset(rule_set)
    return setup


# pattern = RuleSet("standard", "simple_primer")

# pattern.add(Rule("[Close] > [Close(1)]"))
# pattern.add(Rule("[SMA(20)] > [SMA(50)]"))
# pattern.define_action(Action=Prime("Pattern detected. State Primed"))

# conf = RuleSet("primed", "simple_conf")
# conf.add(Rule("[Close] > [yesterdays High]"))
# conf.define_action(Action=Buy("Confirmation detected. Pos entered"))

# pt_exit = RuleSet("held", "simple_exit")
# pt_exit.add(Rule("[Close] < [yesterdays Close]"))
# pt_exit.add(Rule("[Close] < [SMA(10)]"))
# pt_exit.define_action(Action=Sell("Exit pattern detected. Sell..."))

# SimpleSetup = Setup([pattern, conf, pt_exit])

# SimpleSetup.name = "SimpleSetup"
