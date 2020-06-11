from typing import Any, Optional

from stack.stack import Stack

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
            The dequeue logic would need to be rewritten so that it can get the first value. To do this two Stacks 
            are needed. One as the normal storage and the other to be able to reverse the Stack to get the first value.
"""


class Queue:
    def __init__(self):
        self._storage = Stack()
    
    def __len__(self) -> int:
        return len(self._storage)

    def enqueue(self, value: Any) -> None:
        self._storage.push(value)

    def dequeue(self) -> Optional[Any]:
        reversed_storage = Stack()

        while self._storage:
            reversed_storage.push(self._storage.pop())

        first_item = reversed_storage.pop()

        while reversed_storage:
            self._storage.push(reversed_storage.pop())

        return first_item
