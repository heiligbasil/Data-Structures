# sys.path.append('../doubly_linked_list')
from doubly_linked_list import *


class Queue:
    def __init__(self):
        self.size = 0
        # Why is our DLL a good choice to store our elements?
        # Because it already has a head and tail which are like the front and back of a Queue
        self.storage = DoublyLinkedList()

    def enqueue(self, value):
        # Should add an item to the back of the queue
        self.storage.add_to_tail(value)
        self.size += 1

    def dequeue(self):
        # Should remove and return an item from the front of the queue
        removed_value = self.storage.remove_from_head()
        if removed_value is not None:
            self.size -= 1
        return removed_value

    def len(self):
        return self.size
