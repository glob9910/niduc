from node import Node

class CableCuttedOffChannel(Node):
    def receive_signal(self, signal):
        pass

    def send_signal(self):
        length = 32
        return [0] * length
