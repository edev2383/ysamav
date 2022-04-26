import uuid
from stockbox.stockbox.domain.setups.setup_list import SetupList
from stockbox.stockbox.domain.users.user_model import UserModel
from stockbox.stockbox.domain.buckets.bucket_list import BucketList


class IUser:
    uuid: uuid.UUID
    risk_profile: any
    fname: str
    lname: str
    email: str
    phone: str

    setups: SetupList
    buckets: BucketList

    def __init__(self, user_model: UserModel):
        self.uuid = user_model.uuid
        self.fname = user_model.fname
        self.lname = user_model.lname
        self.email = user_model.email
        self.phone = user_model.phone

    def load_riskprofile(self):
        self.risk_profile = ""

    def load_setups(self):
        self.setups = SetupList()

    def load_buckets(self):
        self.buckets = BucketList()
