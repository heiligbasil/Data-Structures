from doubly_linked_list import DoublyLinkedList


class Stack:
    def __init__(self):
        self.size = 0
        # Why is our DLL a good choice to store our elements?
        # > Because this structure is made to resize one element at a time on one end
        self.storage = DoublyLinkedList()

    def push(self, value):
        self.size += 1
        self.storage.add_to_head(value)

    def pop(self):
        deleted_node = self.storage.remove_from_head()
        if deleted_node is None:
            self.size -= 1
        return deleted_node

    def len(self):
        return self.storage.length
