from itertools import count
from math import gcd
from typing import List


def factorize(n, list: List):
    if n == 1:
        return
    q = cycle_finding(n)
    list.append(q)
    return factorize(n // q, list)


def cycle_finding(number):
    x = 2
    for cycle in count(1):
        y = x
        for i in range(2 ** cycle):
            x = (x * x + 1) % number
            factor = gcd(x - y, number)
            if factor > 1:
                print("factor is", factor)
                return factor


if __name__ == "__main__":
    num = 93261639153879477691635523519
    list = []
    factorize(num, list)
    print(f"factors of {num}: ", list)
