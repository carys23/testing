import pytest

def string_count(string):
    name = ['a', 'b', 'c']
    count = 0

    for find_name in string:
        if find_name in name:
            count += 1
    return count

@pytest.mark.me
def test_with_my_name():
    assert string_count('carys') == 2
    result = string_count('carys')
    assert type(result) is int

@pytest.mark.people
def test_with_ben():
    assert string_count('ben') == 1

@pytest.mark.people
def test_with_sarah():
    assert string_count('sarah') == 2
