import libnum
from libnum.factorize import factorize


def square_and_multiply(x, c, n):
    c = bin(c)
    z = x

    for i in range(3, len(c)):
        z = z ** 2 % n
        if c[i:i+1] == '1':
            z = z * x % n

    return z


def factoring(n, B):
    a = 2
    for j in range(2, B+1):
        a = square_and_multiply(a, j, n)

    d = libnum.gcd(a-1, n)
    if 1 < d < n:
        return "SUCCESS", d
    return "FAILURE", -11


if __name__ == "__main__":
    n = 15770708441
    B = 180
    status, factor = factoring(n, B)
    if status == "SUCCESS":
        other = n//factor
        print(f"factors of {n}", factor, other,
              f"{factor} * {other} = {factor * other}", n)
    else:
        print(status)
