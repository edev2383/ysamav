from stockbox.stockbox.common.helpers.enums import EResult
from ..base.ulist import Ulist


class Result:
    """Used to enshrine any action or logging the BL will require
    output is currently a placeholder. Since we are keeping the type any
    we can decide how to handle it at runtime when this class is more
    fleshed out
    """

    status: EResult
    output: any

    def __init__(self, status: bool, output: any):
        self.status = self._set_status(status)
        self.output = output

    def _set_status(self, status: bool) -> EResult:
        if status == True:
            return EResult.eSuccess
        return EResult.eFail


class ResultList(Ulist):
    """A list wrap around Results. We can use this class to aggregate
    Results around the business layer. Primary use-case is to collect
    the results from Rules/RuleSets and provide a process result for the
    Setup class"""

    def has_errors(self) -> bool:
        has_errors = False
        for result in self:
            if result.status == EResult.eFail:
                has_errors = True
        return has_errors

    def error_count(self) -> int:
        count = 0
        for result in self:
            if result.status == EResult.eFail:
                count = count + 1
        return count
