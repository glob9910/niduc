import random
from node import Node

# Klasa device implementuje interfejs node
class Device(Node):
    def __init__(self):
        self.signal_length = 32
        self.signal = [0] * self.signal_length


    def receive_signal(self, signal):
        for i in range(self.signal_length):
            self.signal[i] = signal[i] 


    def send_signal(self):
        return self.signal
    

    def create_random_signal(self):
        for i in range(self.signal_length):
            self.signal[i] = random.randint(0, 1)
