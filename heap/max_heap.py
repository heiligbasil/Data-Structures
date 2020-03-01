class Heap:
    def __init__(self):
        """A Heap is a special Tree-based data structure in which the tree is a complete binary
        tree. Max-Heap: In a Max-Heap the key present at the root node must be greatest among the
        keys present at all of it’s children. The same property must be recursively true for all
        sub-trees in that Binary Tree"""
        self.storage = []

    def insert(self, value):
        """This adds the input value into the heap; this method should ensure
        that the inserted value is in the correct spot in the heap"""
        # First add the new value to the end of the list
        self.storage.append(value)
        # Must check the validity of the placement of that value
        self._bubble_up(len(self.storage))

    def delete(self):
        """This removes and returns the 'topmost' value from the heap; this
        method needs to ensure that the heap property is maintained after the
        topmost element has been removed"""
        # Swap the topmost root node with the last leaf
        self.storage[0], self.storage[-1] = self.storage[-1], self.storage[0]
        # Remove the last leaf
        del self.storage[-1]

    def get_max(self):
        """This returns the maximum value in the heap in constant time"""
        return self.storage[0]

    def get_size(self):
        """This returns the number of elements stored in the heap"""
        return len(self.storage)

    def _bubble_up(self, index):
        """This moves the element at the specified index "up" the heap by
        swapping it with its parent if the parent's value is less than the
        value at the specified index"""
        # Formula: i parent = (i - 1) / 2
        this = self.storage[index]
        parent_formula = (index - 1) / 2
        parent = self.storage[parent_formula]
        if this > parent:
            # Child value is bigger than the parent value, so swap them
            self.storage[index], self.storage[parent_formula] = self.storage[parent_formula], self.storage[index]

    def _sift_down(self, index):
        """This grabs the indices of this element's children and determines
        which child has a larger value. If the larger child's value is larger
        than the parent's value, the child element is swapped with the parent"""
        # Formula: i left = 2i +1; i right = 2i + 2
        this = self.storage[index]
        left_child_formula = (2 * index) + 1
        right_child_formula = (2 * index) + 2
        left_child = self.storage[left_child_formula]
        right_child = self.storage[right_child_formula]
        if this < left_child and left_child >= right_child:
            # Swap values with the left child if it is bigger
            self.storage[index], self.storage[left_child_formula] = self.storage[left_child_formula], self.storage[index]
        elif this < right_child:
            # Swap values with the right child if it is bigger
            self.storage[index], self.storage[right_child_formula] = self.storage[right_child_formula], self.storage[index]
