def cgcd(a, b):
    r0, r1 = a, b
    list = []
    while b > 0:
        q = a // b
        list.append(q)
        s = b
        b = a - q*b
        a = s

    return dict(a=r0, b=r1, cgd=a, quotients=list)

def wiener(n, b):
    return

print(cgcd(42, 105))
