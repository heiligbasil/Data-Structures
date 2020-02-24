class ListNode:
    """Each ListNode holds a reference to its previous node
    as well as its next node in the List."""

    def __init__(self, value, prev=None, next=None):
        self.value = value
        self.prev = prev
        self.next = next

    def insert_after(self, value):
        """Wrap the given value in a ListNode and insert it
        after this node. Note that this node could already
        have a next node it is pointing to."""
        current_next = self.next
        self.next = ListNode(value, self, current_next)
        if current_next:
            current_next.prev = self.next

    def insert_before(self, value):
        """Wrap the given value in a ListNode and insert it
        before this node. Note that this node could already
        have a previous node it is pointing to."""
        current_prev = self.prev
        self.prev = ListNode(value, current_prev, self)
        if current_prev:
            current_prev.next = self.prev

    def delete(self):
        """Rearranges this ListNode's previous and next pointers
        accordingly, effectively deleting this ListNode."""
        if self.prev:
            self.prev.next = self.next
        if self.next:
            self.next.prev = self.prev


class DoublyLinkedList:
    """Our doubly-linked list class. It holds references to
    the list's head and tail nodes."""

    def __init__(self, node=None):
        self.head = node
        self.tail = node
        self.length = 1 if node is not None else 0

    def __len__(self):
        return self.length

    def add_to_head(self, value):
        """Wraps the given value in a ListNode and inserts it
        as the new head of the list. Don't forget to handle
        the old head node's previous pointer accordingly."""
        self.length += 1
        if not self.head and not self.tail:
            # Empty list (no head or tail) so this node becomes its own head and tail
            self.head = self.tail = ListNode(value)
        else:
            # We know that the list is populated
            self.head.insert_before(value)
            self.head = self.head.prev

    def remove_from_head(self):
        """Removes the List's current head node, making the
        current head's next node the new head of the List.
        Returns the value of the removed Node."""
        value = self.head.value
        self.delete(self.head)
        return value

    def add_to_tail(self, value):
        """Wraps the given value in a ListNode and inserts it
        as the new tail of the list. Don't forget to handle
        the old tail node's next pointer accordingly."""
        self.length += 1
        if not self.head and not self.tail:
            self.head = self.tail = ListNode(value)
        else:
            self.tail.insert_after(value)
            self.tail = self.tail.next

    def remove_from_tail(self):
        """Removes the List's current tail node, making the
        current tail's previous node the new tail of the List.
        Returns the value of the removed Node."""
        value = self.tail.value
        self.delete(self.tail)
        return value

    def move_to_front(self, node):
        """Removes the input node from its current spot in the
        List and inserts it as the new head node of the List."""
        # if node is self.head:
        #     return
        # value = node.value
        # if node is self.tail:
        #     self.remove_from_tail()
        # else:
        #     node.delete()
        # self.add_to_head(value)
        self.delete(node)
        self.add_to_head(node.value)

    def move_to_end(self, node):
        """Removes the input node from its current spot in the
        List and inserts it as the new tail node of the List."""
        self.delete(node)
        self.add_to_tail(node.value)

    def delete(self, node):
        """Removes a node from the list and handles cases where
        the node was the head or the tail"""
        # Planning: When the linked list is empty
        if not self.head and not self.tail:
            print('ERROR: Attempted to delete node not in list!')
            return
        # When the node is both head and tail
        elif self.head == self.tail:
            self.head = None
            self.tail = None
        # When the node is head
        elif node == self.head:
            self.head = self.head.next
            node.delete()
        # When the node is tail
        elif node == self.tail:
            self.tail = self.tail.prev
            node.delete()
        # When the node is in the middle
        else:
            node.delete()
        self.length -= 1

    def get_max(self):
        """Returns the highest value currently in the list"""
        # Plan: Make max var, loop through nodes via node.next
        # If node.value is higher, update max
        # Return max
        max_value = self.head.value
        current_node = self.head
        for i in range(self.length):
            if current_node.value > max_value:
                max_value = current_node.value
            current_node = current_node.next
        return max_value
