def sumDigitSquare(n):
    s = 0
    while (n != 0):
        digit = n % 10
        s += digit * digit
        n = n // 10

    return s

def Happy(n):
    set_n=set()
    set_n.add(n)
    while (True):
