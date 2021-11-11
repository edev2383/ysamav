from stockbox.stockbox.domain.rules.ruleset import RuleSet
from ...common.base.ulist import Ulist
from stockbox.stockbox.common.helpers.enums import EBucket


class RuleSetList(Ulist):
    def find(self, bucket: EBucket) -> RuleSet:
        for ruleset in self:
            if ruleset.bucket == bucket:
                return ruleset
        return None
