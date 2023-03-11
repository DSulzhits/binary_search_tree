import pytest
from lesson_14_2.src.binary_search_tree import BinarySearchTree

@pytest.fixture
def bst():
    bst = BinarySearchTree()
    bst.insert({'id': 40})
    return bst


def test_bst_empty():
    """В пустом дереве root ссылается на None"""
    bst = BinarySearchTree()
    assert bst.root is None


def test_bst_insert_root(bst):
    """При добавлении единственного узла он хранится в root"""
    assert bst.root.data == {'id': 40}

def test_bst_insert_left(bst):
    """Добавляем первый элемент слева"""
    bst.insert({'id': 30})
    assert bst.root.left.data == {'id': 30}

def test_bst_insert_right(bst):
    """Добавляем первый элемент слева"""
    bst.insert({'id': 50})
    assert bst.root.right.data == {'id': 50}