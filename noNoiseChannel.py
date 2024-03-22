from node import Node

class NoNoiseChannel(Node):
    def __init__(self):
        self.signal_length = 32
        self.signal = [0] * self.signal_length
        
    def receive_signal(self, signal):
        for i in range(self.signal_length):
            self.signal[i] = signal[i] 


    def send_signal(self):
        return self.signal
