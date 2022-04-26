from stockbox.stockbox.common.helpers.enums import EBucket


class IAction:
    to_bucket: EBucket

    def transition(self):
        ...
