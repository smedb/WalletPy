from models.trigger import Trigger
from constants.trigger_constants import TriggerConstants


class TriggerController(TriggerConstants):
    def __init__(self):
        self.triggers = Trigger()
        
    def create_trigger(self, name: str, amount: int, action: int):
        trigger = Trigger()
        
        trigger.name = name
        trigger.amount = amount
        trigger.action = action
        
        trigger.save()