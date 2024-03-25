"""Virus"""
def virus():
    """Virus1"""
    text = input()
    start = 0
    for char in text:
        if char == 'o':
            start += 1
    print(start)
virus()
