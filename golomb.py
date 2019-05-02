import math

def unary(val):
    v = '1' * val + '0'
    return v
    


def encode(m, n):
    k = math.floor(math.log2(m))
    r = n % m
    t = 2**k - m
    code = unary(int(n / m))
    if r < t:
        val = bin(r)[3:]
        val = "0" * (k - 1) + val
        return code + val 
    else:
        r += t
        val = bin(r)[3:]
        val = "0" * k + val
        return code + val

print(encode(7, 8))
print(encode(10, 20))
