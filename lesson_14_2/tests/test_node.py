from lesson_14_2.src.node import Node


def test_node_init():
    data = {'id': 1}
    node = Node(data)
    assert node.data == data
    assert node.left is None
    assert node.right is None
