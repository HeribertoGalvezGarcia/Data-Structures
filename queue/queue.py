from typing import Any, Optional

from singly_linked_list.singly_linked_list import LinkedList

"""
A queue is a data structure whose primary purpose is to store and
return elements in First In First Out order. 

1. Implement the Queue class using an array as the underlying storage structure.
   Make sure the Queue tests pass.
2. Re-implement the Queue class, this time using the linked list implementation
   as the underlying storage structure.
   Make sure the Queue tests pass.
3. What is the difference between using an array vs. a linked list when 
   implementing a Queue? Using different method names and using slightly different logic for pop
   
Stretch: What if you could only use instances of your Stack class to implement the Queue?
         What would that look like? How many Stacks would you need? Try it!
"""


class Queue:
    def __init__(self):
        self._storage = LinkedList()
    
    def __len__(self) -> int:
        return len(self._storage)

    def enqueue(self, value: Any) -> None:
        self._storage.add_to_tail(value)

    def dequeue(self) -> Optional[Any]:
        return self._storage.remove_head()
