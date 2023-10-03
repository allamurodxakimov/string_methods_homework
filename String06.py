def main(s):
    """
    A variable of type str is given. Check that it consists only of numbers.
    Args:
        s: str
    Returns:
        bool: answer
    """
    
    return s.isdigit()
print(main("123454324"))
print(main("12345432 d"))