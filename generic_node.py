class GenericNode:
    """Class for the construction of Nodes"""

    def __init__(self, this_value):
        """Default constructor for instantiation"""
        self.value = this_value
        self.next = None

    def add(self, this_value):
        """Create a new node and attach it to this one"""
        self.next = GenericNode(this_value)

    def reverse(self):
        """Reverse the flow of the list, making the head the tail and the old tail the head"""
        current_node = self  # The starting node, by definition it is the Head
        new_node = current_node.next  # The new node will be the cursor
        current_node.next = None  # Turn the head into the tail by removing its Next pointer
        while new_node is not None:  # Loop as long as the tail hasn't been reached
            previous_node = current_node  # Store this temporarily for shuffling the pointers
            current_node = new_node  #
            new_node = current_node.next
            current_node.next = previous_node
        return current_node

    def locate_midpoint_value(self):
        """Traverse the list once to find the midpoint and return the value"""
        middle_node = self  # The middle node, initially set to the starting node
        end_node = self  # The last node reached, initially set to the starting node
        while end_node is not None:  # Loop as long as the Tail hasn't been reached
            end_node = end_node.next  # Keep refreshing this with the last node
            if end_node:
                end_node = end_node.next
                middle_node = middle_node.next
        return middle_node.value


root = GenericNode(1)
nl = root
nl.add(2)
nl = nl.next
nl.add(3)
nl = nl.next
nl.add(4)
nl = nl.next
nl.add(5)
nl = nl.next
nl.add(6)
nl = nl.next
nl.add(7)
nl = nl.next
nl.add(8)
nl = nl.next
cur = root
print('Regular direction:',end=' | ')
while cur:
    print(cur.value,end=' ')
    cur = cur.next
    print('|',end=' ')
print(f'\nMiddle value: {root.locate_midpoint_value()}')
cur = root.reverse()
mid = cur
print('Reverse direction:',end=' | ')
while cur:
    print(cur.value,end=' ')
    cur = cur.next
    print('|',end=' ')
print(f'\nMiddle value: {mid.locate_midpoint_value()}')