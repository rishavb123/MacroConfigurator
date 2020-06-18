class Trigger:
    def __init__(self, macro):
        self.active = False
        self.macro = macro
    
    def trigger(self, config):
        self.macro.start(config)

    def check(self, s):
        print("Using default check that just returns False")
        return False

    def run(self, s):
        if self.check(s):
            self.trigger(s)