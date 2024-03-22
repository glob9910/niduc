from abc import ABC, abstractmethod

# ABC - abstract class, Node jest interfejsem z dwoma metodami
class Node(ABC):
    @abstractmethod
    def receive_signal(self, signal):
        pass

    @abstractmethod
    def send_signal(self):
        pass
