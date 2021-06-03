import pytest
from datetime import datetime
import pytz
from question_1 import Node, Queue

SIZE_QUEUE = 7


@pytest.fixture
def node_element():
    node_1 = Node("node_1")
    return node_1


def test_node(node_element):
    assert node_element.data == "node_1"
    assert isinstance(node_element.addition_time, datetime)


def test_node_addition_time():
    now_datetime = datetime.now(tz=pytz.utc)
    node = Node(None, now_datetime)
    assert now_datetime == node.addition_time


@pytest.fixture
def queue_data():
    queue = Queue()
    for x in range(SIZE_QUEUE):
        queue.push(x)
    return queue


def test_queue_size(queue_data):
    assert queue_data.size == SIZE_QUEUE


def test_queue_push(queue_data):
    for x in range(SIZE_QUEUE):
        queue_data.pop()
    queue_data.push(10)
    assert queue_data.size == 1
    last = queue_data.pop()
    assert last.data == 10
    assert queue_data.size == 0


def test_queue_first_in_first_out(queue_data):
    last = queue_data.pop()
    assert last.data == 0
    assert queue_data.size == SIZE_QUEUE - 1


def test_queue_next(queue_data):
    last = queue_data.pop()
    assert last.next.data == 1
    last = queue_data.pop()
    assert last.next.data == 2


def test_queue_tail_head(queue_data):
    assert queue_data.head.data == 0
    queue_data.pop()
    queue_data.pop()
    assert queue_data.head.data == 2


def test_queue_tail(queue_data):
    assert queue_data.tail.data == 6
    queue_data.push(15)
    assert queue_data.tail.data == 15
    assert queue_data.size == SIZE_QUEUE + 1
