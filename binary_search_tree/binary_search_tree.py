from __future__ import annotations

from typing import Any, Optional

"""
Binary search trees are a data structure that enforce an ordering over 
the data they store. That ordering in turn makes it a lot more efficient 
at searching for a particular piece of data in the tree. 

This part of the project comprises two days:
1. Implement the methods `insert`, `contains`, `get_max`, and `for_each`
   on the BSTNode class.
2. Implement the `in_order_print`, `bft_print`, and `dft_print` methods
   on the BSTNode class.
"""


class BSTNode:
    left: Optional[BSTNode]
    right: Optional[BSTNode]

    def __init__(self, value: Any) -> None:
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value: Any) -> None:
        side = 'left' if value < self.value else 'right'

        if (side_node := getattr(self, side)) is None:
            setattr(self, side, BSTNode(value))
        else:
            side_node.insert(value)

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target: Any) -> bool:
        if target == self.value:
            return True

        side = 'left' if target < self.value else 'right'
        if (side_node := getattr(self, side)) is not None:
            return side_node.contains(target)

        return False

    # Return the maximum value found in the tree
    def get_max(self) -> Any:
        return self.value if self.right is None else self.right.get_max()

    # Call the function `fn` on the value of each node
    def for_each(self, fn):
        fn(self.value)
        for node in (self.left, self.right):
            if node is not None:
                node.for_each(fn)

    # Part 2 -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    @staticmethod
    def in_order_print(node: BSTNode) -> None:
        if node.left is not None:
            node.left.in_order_print(node.left)

        print(node.value)

        if node.right is not None:
            node.right.in_order_print(node.right)

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self, node: BSTNode) -> None:
        if node is self:
            print(node.value)

        nodes = (node.right, node.left)

        for sub_node in nodes:
            if sub_node is not None:
                print(sub_node.value)

        for sub_node in nodes:
            if sub_node is not None:
                self.bft_print(sub_node)

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self, node: BSTNode) -> None:
        print(node.value)

        for sub_node in (node.left, node.right):
            if sub_node is not None:
                self.dft_print(sub_node)

    # Stretch Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT
    def pre_order_dft(self, node):
        print(node.value)

        for sub_node in (node.left, node.right):
            if sub_node is not None:
                self.pre_order_dft(sub_node)

    # Print Post-order recursive DFT
    def post_order_dft(self, node: BSTNode) -> None:
        for sub_node in (node.left, node.right):
            if sub_node is not None:
                self.post_order_dft(sub_node)

        print(node.value)
