from Lib.SubEngine import SubEngine
from Lib.Objects.Display import Display



class FrameMaster(SubEngine):

    def __init__(self, pPort):
        super().__init__("FrameMaster", 1)
        self.port = pPort
        self.display = None

    def setup(self):
        self.display = Display(self.pixellength, 0, self.port)
        self.display.startServer()

    def terminate(self):
        self.display.stopServer()


    def update(self):
        self.display.update()

    def onMessage(self, topic, payload):
        if topic == "TERMINATE" and payload == "TERMINATE":
            self.display.stopServer()

    def getStates(self):
        return None