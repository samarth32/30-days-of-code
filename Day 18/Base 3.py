def convertToTernary(N):
    if (N == 0):
        return

    x = N % 3
    N //= 3
    if (x < 0):
        N += 1


    convertToTernary(N)


    if (x < 0):
        print(x + (3 * -1), end="")
    else:
        print(x, end="")


def convert(Decimal):


    if (Decimal != 0):
        convertToTernary(Decimal)
    else:
        print("0", end="")


n = int(input())
convert(n)
