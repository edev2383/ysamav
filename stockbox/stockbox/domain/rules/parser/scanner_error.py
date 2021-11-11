from ....common.base.ulist import Ulist


class ScannerError:
    def __init__(self, message: str):
        self.message = message


class ScannerErrorList(Ulist):
    pass
