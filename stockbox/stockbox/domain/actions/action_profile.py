from numpy import double
from .i_action import IAction


class ActionProfile:
    """The action profile contains all of the action information for
    interfacing with the API. How many shares to buy/sell, the type of
    action, etc etc. These are calculated at runtime based on the risk profile
    and the position/controller"""

    shares: int
    price_market: double
    price_limit: double
    action: IAction
    action_expiration: int # seconds
    
    pass
