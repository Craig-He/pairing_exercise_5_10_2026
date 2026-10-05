import pytest

def test_includes_todo_empty():
    assert includes_todo("") == False

def test_includes_todo_one_line():
    assert includes_todo("#TODO buy milk")

def test_includes_todo_one_line_false():
    assert includes_todo("buy milk")

def test_includes_todo_multiple_lines():
    text = "go to the shops\n#TODO buy milk\ngo home"

    assert includes_todo(text)

def test_includes_todo_multiple_lines_false():
    text = "go to the shops\n#buy milk\ngo home"

    assert not includes_todo(text)

def test_includes_todo_incorrect_datatype():
    with pytest.raises(ValueError):
        includes_todo(1.0)

