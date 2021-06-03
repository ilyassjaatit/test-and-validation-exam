"""
    Implement a class FIFO (First in First Out).
    It should be a class with the following methods:
    1. push: add an element to the class.
    2. pop: get and remove the oldest element.
    3. size: get the number of elements
    4. addition_time: get the datetime when any element present on the FIFO was added.
"""
from datetime import datetime
import pytz


class Node(object):
    """
    A class represent node,
    The times are worked in utc-0 and are transformed into local time
    ...
    Parameters:
        data : str
            Any data (default None)
        addition_time : datetime
            Creation (default  datetime utc-0)
        next:
            next node (default None)
    """

    def __init__(self, data=None, addition_time=datetime.now(tz=pytz.utc), next=None):
        self.data = data
        self.addition_time = addition_time
        self.next = next


class Queue(object):
    """
    Queue list based in nodes
    ...
    Parameters:
        head: First item in the queue
        tail: Last item in queue
        size: Tamaño de la cola

    """

    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def push(self, data):
        node = Node(data)
        if self.head is None:
            self.head = node
            self.tail = self.head
        else:
            self.tail.next = node
            self.tail = node
        self.size += 1

    def pop(self):
        current = self.head
        if self.size == 1:
            self.size -= 1
            self.head = None
            self.tail = None
        elif self.size > 1:
            self.head = self.head.next
            self.size -= 1
        return current
