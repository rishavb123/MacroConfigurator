from triggers.trigger import Trigger

class TriggerWithHandler(Trigger):

    def __init__(self, handler):
        super().__init__()
        self.handler = handler # has method signature handler(trigger)

    def trigger(self):
        self.handler(self)