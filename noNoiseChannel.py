from node import Node

class NoNoiseChannel(Node):
    
    def __init__(self):
        self.signal_length = 32
        self.number_of_signals=2
        self.signal = [[0] * self.signal_length]
        self.data = self.signal *self.number_of_signals

    def receive_signal(self, data):
        for i in range(len(data)):
            for j in range(len(data[i])):
                self.data[i][j]=data[i][j]

    def send_signal(self):
        return self.data
