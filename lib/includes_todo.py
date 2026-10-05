def includes_todo(text: str)->bool:
    if not isinstance(text, str):
        raise ValueError
    return any(x.startswith('#TODO') for x in text.split('\n'))
    
