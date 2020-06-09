from __future__ import annotations

from typing import Any, Optional


class ListNode:
    """Each ListNode holds a reference to its previous node
    as well as its next node in the List.
    """

    def __init__(self, value: Any, prev: ListNode = None, next_: ListNode = None) -> None:
        self.value = value
        self.prev = prev
        self.next = next_

    def insert_after(self, value: Any) -> None:
        """Wrap the given value in a ListNode and insert it
        after this node. Note that this node could already
        have a next node it is point to.
        """

        current_next = self.next
        self.next = ListNode(value, self, current_next)

        if current_next is not None:
            current_next.prev = self.next

    def insert_before(self, value: Any) -> None:
        """Wrap the given value in a ListNode and insert it
        before this node. Note that this node could already
        have a previous node it is point to.
        """

        current_prev = self.prev
        self.prev = ListNode(value, current_prev, self)

        if current_prev is not None:
            current_prev.next = self.prev

    def delete(self) -> None:
        """Rearranges this ListNode's previous and next pointers
        accordingly, effectively deleting this ListNode.
        """

        if self.prev is not None:
            self.prev.next = self.next

        if self.next is not None:
            self.next.prev = self.prev


class DoublyLinkedList:
    """Our doubly-linked list class. It holds references to
    the list's head and tail nodes.
    """

    def __init__(self, node: ListNode = None) -> None:
        self.head = self.tail = node

    def __iter__(self) -> DoublyLinkedList:
        self._current = self.head
        return self

    def __next__(self) -> ListNode:
        if (current := self._current) is None:
            raise StopIteration

        self._current = current.next
        return current

    def __len__(self) -> int:
        return sum(1 for _ in self)

    def add_to_head(self, value: Any) -> None:
        """Wraps the given value in a ListNode and inserts it
        as the new head of the list. Don't forget to handle
        the old head node's previous pointer accordingly.
        """

        if self.head is not None:
            self.head.insert_before(value)
            self.head = self.head.prev
        else:
            self.head = self.tail = ListNode(value)

    def remove_from_head(self) -> Optional[Any]:
        """Removes the List's current head node, making the
        current head's next node the new head of the List.
        Returns the value of the removed Node.
        """

        if (current := self.head) is None:
            return None

        self.head = next_node = current.next

        if next_node is None:
            self.tail = None

        return current.value

    def add_to_tail(self, value: Any) -> None:
        """Wraps the given value in a ListNode and inserts it
        as the new tail of the list. Don't forget to handle
        the old tail node's next pointer accordingly.
        """

        if self.tail is not None:
            self.tail.insert_after(value)
            self.tail = self.tail.next
        else:
            self.head = self.tail = ListNode(value)

    def remove_from_tail(self) -> Optional[Any]:
        """Removes the List's current tail node, making the
        current tail's previous node the new tail of the List.
        Returns the value of the removed Node.
        """

        if (current := self.tail) is None:
            return None

        self.tail = prev_node = current.prev

        if prev_node is None:
            self.head = None

        return current.value

    def move_to_front(self, node: ListNode) -> None:
        """Removes the input node from its current spot in the
        List and inserts it as the new head node of the List.
        """

        self.delete(node)

        if (head := self.head) is not None:
            head.prev = node

        node.next = head
        node.prev = None

        self.head = node

    def move_to_end(self, node: ListNode) -> None:
        """Removes the input node from its current spot in the
        List and inserts it as the new tail node of the List.
        """

        self.delete(node)

        if (tail := self.tail) is not None:
            tail.next = node

        node.prev = tail
        node.next = None

        self.tail = node

    def delete(self, node: ListNode) -> None:
        """Removes a node from the list and handles cases where
        the node was the head or the tail
        """

        node.delete()
        if node is self.head:
            self.head = node.next
        if node is self.tail:
            self.tail = node.prev

    def get_max(self) -> Optional[Any]:
        """Returns the highest value currently in the list"""

        if self.head is None:
            return None

        return max(node.value for node in self)
