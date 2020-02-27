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

    def for_each(self, cb):
        """This performs a traversal of EVERY node in the tree,
        executing the passed-in callback function on each tree node value.
        There is a myriad of ways to perform tree traversal;
        in this case any of them should work.
        Call the function `cb` on the value of each node.
        You may use a recursive or an iterative approach"""
        pass

    # DAY 2 Project -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self, node):
        pass

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self, node):
        pass

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self, node):
        pass

    # STRETCH Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT
    def pre_order_dft(self, node):
        pass

    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        pass


bst = BinarySearchTree(10)
bst.insert(5)
bst.insert(15)
bst.insert(4)
bst.insert(17)
bst.insert(6)
bst.insert(13)
bst.contains(6)
bst.contains(14)
bst.get_max()
