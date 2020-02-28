import sys

sys.path.append('../queue_and_stack')
from dll_queue import Queue
from dll_stack import Stack


class BinarySearchTree:
    """Binary Search Tree, is a node-based binary tree data structure which has the following properties: The left
    subtree of a node contains only nodes with keys lesser than the node’s key. The right subtree of a node contains
    only nodes with keys greater than the node’s key. The left and right subtree each must also be a binary search
    tree. There must be no duplicate nodes """

    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, value):
        """Insert the given value into the tree. Insert adds the input value
        to the binary search tree, adhering to the rules of the ordering of
        elements in a binary search tree"""
        print(f'->INSERTING value {value}')
        if value < self.value:
            # Go left, if the value to insert is less than the root
            if self.left is None:
                # Create a new node if there isn't one
                self.left = BinarySearchTree(value)
                print('left node added')
            else:
                # Recursively call this function on the node to the left
                print('left node traversal...')
                self.left.insert(value)
        else:
            # Go right, if the value to insert is less than or equal to the root
            if self.right is None:
                # Create a new node if the right node is nonexistent
                self.right = BinarySearchTree(value)
                print('right node added')
            else:
                # If it exists, call this function recursively using the node on the right as the perceived root
                print('right node traversal...')
                self.right.insert(value)

    def insert_guided_lecture_solution(self, value):
        """Insert the given value into the tree. Insert adds the input value
        to the binary search tree, adhering to the rules of the ordering of
        elements in a binary search tree"""
        if value < self.value:
            if self.left:
                self.left.insert_guided_lecture_solution(value)
            else:
                self.left = BinarySearchTree(value)
        if value >= self.value:
            if self.right:
                self.right.insert_guided_lecture_solution(value)
            else:
                self.right = BinarySearchTree(value)

    def contains(self, target):
        """This searches the binary search tree for the input value,
        returning a boolean indicating whether the value exists in the
        tree or not"""
        print(f'00LOOKING for value {target}')
        if self.value == target:
            # Found the target value
            print('found the target')
            return True
        elif self.value > target:
            # Go left if the target is less
            print('left node traversal...')
            if self.left is None:
                # First see if the left node is empty; if not, the target doesn't exist
                print('target does NOT exist')
                return False
            else:
                # Verified the left node exists; now can call this method on it
                return self.left.contains(target)
        else:
            # Go right when the target is greater than or equal to the value of the current node
            print('right node traversal...')
            if self.right is None:
                # First see if the right node is empty; if not, the target doesn't exist
                print('target does NOT exist')
                return False
            else:
                # Verified the right node exists; now can call this method on it
                return self.right.contains(target)

    def contains_guided_lecture_solution(self, target):
        """This searches the binary search tree for the input value,
        returning a boolean indicating whether the value exists in the
        tree or not"""
        if self.value == target:
            return True
        if self.value > target:
            if self.left:
                return self.left.contains_guided_lecture_solution(target)
            else:
                return False
        if self.value <= target:
            if self.right:
                return self.right.contains_guided_lecture_solution(target)
            else:
                return False

    def get_max(self):
        """This returns the maximum value in the binary search tree"""
        print('^^MAX value')
        if self.right is None:
            # No more nodes to the right; found the largest value
            print(f'max value is {self.value}')
            return self.value
        else:
            # Keep traversing the nodes to the right in search of the final one
            print('traversing to the right...')
            return self.right.get_max()

    def get_max_guided_lecture_solution(self):
        """This returns the maximum value in the binary search tree"""
        if not self.right:
            return self.value
        else:
            return self.right.get_max_guided_lecture_solution()

    def for_each(self, cb, cb2=lambda x: arr_neg.append(-x)):
        """This performs a traversal of EVERY node in the tree,
        executing the passed-in callback function on each tree node value.
        There is a myriad of ways to perform tree traversal;
        in this case any of them should work.
        Call the function `cb` on the value of each node.
        You may use a recursive or an iterative approach"""
        print('xxFOR_EACH')
        # First, put the value of the node into the callback function
        cb(self.value)
        cb2(self.value)
        if self.left is not None:
            # After the left node is verified to be existing, call this method with the callback
            print('traversing to the left')
            self.left.for_each(cb, cb2)
        if self.right is not None:
            # After the right node is verified to be existing, call this method with the callback
            print('traversing to the right')
            self.right.for_each(cb, cb2)

    def for_each_guided_lecture_solution(self, cb, cb2=lambda x: arr_neg.append(-x)):
        """This performs a traversal of EVERY node in the tree,
        executing the passed-in callback function on each tree node value.
        There is a myriad of ways to perform tree traversal;
        in this case any of them should work.
        Call the function `cb` on the value of each node.
        You may use a recursive or an iterative approach"""
        cb(self.value)
        if self.left:
            self.left.for_each_guided_lecture_solution(cb)
        if self.right:
            self.right.for_each_guided_lecture_solution(cb)

    # -------------------------------------
    # DAY 2 Project -----------------------
    # -------------------------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self, node):
        if not node.left and not node.right:
            # Print the value when the node is a leaf
            print(node.value)
        if node.left:
            # Traverse left if you can
            self.in_order_print(node.left)
            if not node.right:
                # After returning, print this value to pick up orphan nodes without a right
                print(node.value)
        if node.right:
            # First print the value because the current value should be lower
            print(node.value)
            # Then traverse right
            self.in_order_print(node.right)

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self, node):
        queue = Queue()
        queue.enqueue(node)
        while queue.size > 0:
            this_node = queue.dequeue()
            if this_node is None:
                continue
            print(this_node.value)
            if this_node.right:
                queue.enqueue(this_node.right)
            if this_node.left:
                queue.enqueue(this_node.left)

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self, node):
        stack = Stack()
        stack.push(node)
        while stack.size > 0:
            this_node = stack.pop()
            if this_node is None:
                continue
            print(this_node.value)
            if this_node.right:
                stack.push(this_node.right)
            if this_node.left:
                stack.push(this_node.left)

    # STRETCH Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT
    def pre_order_dft(self, node):
        pass

    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        pass

# bst = BinarySearchTree(10)
# bst.insert_guided_lecture_solution(5)
# bst.insert_guided_lecture_solution(15)
# bst.insert_guided_lecture_solution(4)
# bst.insert_guided_lecture_solution(17)
# bst.insert_guided_lecture_solution(6)
# bst.insert_guided_lecture_solution(13)
# bst.contains(6)
# bst.contains(14)
# bst.get_max()
# arr = []
# arr_neg = []
# cby = lambda x: arr.append(x)
# bst.for_each(cby)
# print(arr)
# print(arr_neg)
# bst.bft_print(bst)
