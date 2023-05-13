from utils import arrs
import pytest


@pytest.fixture
def array_fixture():
    return [1, 2, 3, 4]


def test_get():
    assert arrs.get([1, 2, 3], 1, "test") == 2
    assert arrs.get([], -1, "test") == "test"


def test_slice(array_fixture):
    assert arrs.my_slice(array_fixture, 1, 3) == [2, 3]
    assert arrs.my_slice(array_fixture, -1) == [4]
    assert arrs.my_slice(array_fixture, -5) == [1, 2, 3, 4]
    assert arrs.my_slice(array_fixture, 1) == [2, 3, 4]


def test_slice_empty():
    assert arrs.my_slice([], 1) == []
