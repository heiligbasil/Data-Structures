from generic_node import GenericNode


class SinglyLinkedList:
    """Class for the construction of Singly Linked Lists"""

    def __init__(self, node=None):
        """Default constructor to instantiate this"""
        self.head = node
        self.tail = node
        self.middle = None
        self.size = 0 if node is not None else 1

    def push(self, value):
        """Add a new node to the head/start"""
        node_after_head = None
        if self.head == self.tail:
            self.head = self.tail = GenericNode(value)
        else:
            self.head.add(value)
            self.head.next = self.head.next
        node_to_stick = GenericNode(value, node_after_head)
        self.size += 1

# In progress

#     def pop(self):
#
#
# sll = SinglyLinkedList(1)
# sll.push(2)
# sll.push(3)
# sll.push(4)
# sll.push(5)
#
# current_tail = sll.tail
# original_head = sll.head
# while current_tail != original_head:
#     value = current_tail.pop()
#     sll.push(value)

# Pull off head
# Change head.next to None
# Add to new list
# Pull off new head
# Add to list
# Modify head.next
# Head becomes new tail (find by seeing if it points to None)
# Use variables to store current_value and next_value
