from stockbox.stockbox.domain.controllers.domain_controller import DomainController
from stockbox.stockbox.domain.positions.i_position import IPosition
from .i_action import IAction


class ActionHandler:
    """The action handler will take in the position and the domain
    controller and make decisions based on the RVR Profile, then tell
    the domain controller what to do."""

    position: IPosition
    controller: DomainController


    def __init__(self, position: IPosition, controller: DomainController):
        # from the position, we can get all other information about the
        # stock/setup/result, ROI, etc. At this point, we have a successful
        # setup result
        self.position = position
        # ActionHandler taking in the controller, to tell it what to do
        # based on the details in the action.
        self.controller = controller

    def process(self):
        ...
