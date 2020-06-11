from __future__ import annotations

from typing import Any, Optional


class Node:
    def __init__(self, value: Any = None, next_node: Node = None) -> None:
        self.value = value
        self.next = next_node


class LinkedList:
    head: Optional[Node]
    tail: Optional[Node]

    def __init__(self) -> None:
        self.head = None
        self.tail = None

    def __iter__(self) -> LinkedList:
        self._current = self.head
        return self

    def __next__(self) -> Node:
        if (current := self._current) is None:
            raise StopIteration

        self._current = current.next
        return current

    def __len__(self) -> int:
        return sum(1 for _ in self)

    def add_to_tail(self, value: Any) -> None:
        node = Node(value, None)

        if self.head is None:
            self.head = node
        else:
            self.tail.next = node

        self.tail = node

    def remove_head(self) -> Optional[Any]:
        if (current := self.head) is None:
            return None

        self.head = next_node = current.next

        if next_node is None:
            self.tail = None

        return current.value

    def remove_tail(self) -> Optional[Any]:
        if self.head is None:
            return None

        value = self.tail.value

        if self.head is self.tail:
            self.head = self.tail = None
        else:
            for node in self:
                if node.next is self.tail:
                    self.tail = node
                    self.tail.next = None

        return value

    def contains(self, value: Any) -> bool:
        if self.head is None:
            return False

        return any(value == node.value for node in self)

    def get_max(self) -> Optional[Any]:
        if self.head is None:
            return None

        return max(node.value for node in self)
