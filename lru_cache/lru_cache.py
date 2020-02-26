from doubly_linked_list import *


class LRUCache:
    """
    Our LRUCache class keeps track of the max number of nodes it
    can hold, the current number of nodes it is holding, a doubly-
    linked list that holds the key-value entries in the correct
    order, as well as a storage dict that provides fast access
    to every node stored in the cache.
    """

    def __init__(self, limit=10):
        """
        Default constructor for this class
        """
        self.max_limit = limit
        self.size = 0
        self.order = DoublyLinkedList()
        self.storage = dict()  # or {}

    def get(self, key):
        """
        Retrieves the value associated with the given key. Also
        needs to move the key-value pair to the end of the order
        such that the pair is considered most-recently used.
        Returns the value associated with the key or None if the
        key-value pair doesn't exist in the cache.
        """
        if key not in self.storage.keys():
            return None
        retrieved_value = self.storage[key]
        self.order.move_to_front(retrieved_value)
        return retrieved_value.value

    def get_guided_lecture_solution(self, key):
        """
        Retrieves the value associated with the given key. Also
        needs to move the key-value pair to the end of the order
        such that the pair is considered most-recently used.
        Returns the value associated with the key or None if the
        key-value pair doesn't exist in the cache.
        """
        # If key is in the storage
        if key in self.storage:
            # Move it to the end
            node = self.storage[key]
            self.order.move_to_end(node)
            # Return the value
            return node.value[1]
        # If the key is not in the storage
        else:
            # Return None
            return None

    def set(self, key, value):
        """
        Adds the given key-value pair to the cache. The newly-
        added pair should be considered the most-recently used
        entry in the cache. If the cache is already at max capacity
        before this entry is added, then the oldest entry in the
        cache needs to be removed to make room. Additionally, in the
        case that the key already exists in the cache, we simply
        want to overwrite the old value associated with the key with
        the newly-specified value.
        """
        if key in self.storage.keys():
            node_to_update = self.storage[key]
            self.order.delete(node_to_update)
            self.order.add_to_head(value)
            self.storage[key] = self.order.head
        else:
            if self.size == self.max_limit:
                tail_node_key = next(k for k, v in self.storage.items() if v == self.order.tail)
                self.storage.pop(tail_node_key)
                self.order.remove_from_tail()
            else:
                self.size += 1
            self.order.add_to_head(value)
            self.storage[key] = self.order.head

    def set_guided_lecture_solution(self, key, value):
        """
        Adds the given key-value pair to the cache. The newly-
        added pair should be considered the most-recently used
        entry in the cache. If the cache is already at max capacity
        before this entry is added, then the oldest entry in the
        cache needs to be removed to make room. Additionally, in the
        case that the key already exists in the cache, we simply
        want to overwrite the old value associated with the key with
        the newly-specified value.
        """
        # Plan out the possible states:
        # Check and see if the key is in the dictionary
        if key in self.storage:
            # If it is:
            node = self.storage[key]
            # Overwrite the value
            node.value = (key, value)
            # Move it to the front
            self.order.move_to_end(node)
            # Nothing else to do, so exit the function
            return
        # If the cache is full:
        if self.size == self.max_limit:
            # Check and see if the cache is full
            # Remove the oldest entry in the dictionary
            del self.storage[self.order.head.value[0]]
            # Remove the oldest entry from the linked list
            self.order.remove_from_head()
            # Reduce the size
            self.size -= 1
        # Add to the linked list (key and the value)
        self.order.add_to_tail((key, value))
        # Add the key and value to the dictionary
        self.storage[key] = self.order.tail
        # Increment the size
        self.size += 1
