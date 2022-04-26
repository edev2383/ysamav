from ...common.base.ulist import Ulist


class IndicatorCollection(Ulist):
    def exists(self, key: str):
        for indicator in self:
            if indicator.df_colkey == key:
                return True
        return False
