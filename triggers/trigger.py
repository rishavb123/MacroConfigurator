
class Trigger:
    def __init__(self, macro):
        self.active = False
        self.macro = macro
    
    def trigger(self, config):
        self.macro.run(config)
