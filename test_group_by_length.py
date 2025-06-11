import pytest
from group_by_length import group_by_length

def test_empty_list():
    assert group_by_length([]) == {}

def test_same_strings():
    assert group_by_length(["a", "a", "a"]) == {1: ["a", "a", "a"]}

def test_varied_lengths():
    data = ["apple", "bat", "car", "boat"]
    assert group_by_length(data) == {3: ["bat", "car"], 4: ["boat"], 5: ["apple"]}

def test_invalid_input():
    with pytest.raises(TypeError):
        group_by_length("not a list")
