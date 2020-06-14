from multiprocessing import Process

class Macro:
    def __init__(self):
        super().__init__()

    def start(self, config):
        Process(target=self.run, args=config).start()

    def run(self, config):
        print("Still using default run. Override this method to create a macro")
