## 1. Describe the Problem

As a user
So that I can find my tasks among all my notes
I want to check if a line from my notes includes the string `#TODO`.

## 2. Design the Function Signature

```python

def includes_todo(tasks: str) -> bool:
    """
    Checks if a line of tasks begins with to-do

    Parameters:
        tasks: string containing tasks

    Returns:
        Boolean representing whether a line of tasks begins with todo

    Side Effecs:
        None
    """
    pass

```

## 3. Create Examples as Tests

```python

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
    assert includes_text(1.0) == ValueError()
```
