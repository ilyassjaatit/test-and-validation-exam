"""
Implement a class FIFO (First in First Out). It should be a class with the following methods:
    1. Implement a class FIFO (First in First Out). It should be a class with the following methods:
    2. pop: get and remove the oldest element.
    3. size: get the number of elements
    4. addition_time: get the datetime when any element present on the FIFO was added.
        If no position is specified by default return last element addition.
"""
from datetime import datetime
import pytz


class Node(object):
    """
    A class represent node,
    The times are worked in utc-0 and are transformed into local time
    ...

    data : str
        Any data (default None)
    addition_time : datetime
        Creation (default  datetime utc-0)
    """

    def __init__(self, data=None, addition_time=datetime.now(tz=pytz.utc)):
        self.data = data
        self.addition_time = addition_time


class Queue(object):
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def push(self, data):
        pass

    def pop(self):
        pass
