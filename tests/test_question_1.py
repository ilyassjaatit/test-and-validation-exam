import pytest
from datetime import datetime
import pytz
from question_1 import Node


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
