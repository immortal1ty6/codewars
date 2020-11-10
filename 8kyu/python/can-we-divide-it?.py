def is_divide_by(number, a, b):
    c = number % a
    d = number % b
    if c == 0 and d == 0:
        return True
    else:
        return False
