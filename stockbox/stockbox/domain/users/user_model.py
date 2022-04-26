import uuid
from dataclasses import dataclass


@dataclass
class UserModel:
    uuid: uuid.UUID
    fname: str
    lname: str
    email: str
    phone: str
