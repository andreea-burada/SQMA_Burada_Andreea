import pytest

ERROR_MESSAGE = "Input must be string."

def removeSpaces(s):
    if not isinstance(s, str):
        raise Exception(ERROR_MESSAGE)
    return s.replace(" ", "")

def test_removeSpaces_string():
    assert removeSpaces(" a   b c  d  ") == "abcd"

def test_removeSpaces_nonstring():
    with pytest.raises(Exception) as e_info:
        removeSpaces(1)
