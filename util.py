n = 20**2 - 9**2
print(n) -> 319

m = (20-9)*(20+9)
print(m) -> 319

# from math import ceil
#
#
# def isqrt(n):
#     x = n
#     y = (x + n // x) // 2
#     while y < x:
#         x = y
#         y = (x + n // x) // 2
#     return x
#
#
# def fermat(n, verbose=True):
#     a = isqrt(n)  # int(ceil(n**0.5))
#     b2 = a*a - n
#     b = isqrt(n)  # int(b2**0.5)
#     count = 0
#     while b*b != b2:
#         if verbose:
#             print('Trying: a=%s b2=%s b=%s' % (a, b2, b))
#         a = a + 1
#         b2 = a*a - n
#         b = isqrt(b2) # int(b2**0.5)
#         count += 1
#     p = a+b
#     q = a-b
#     assert n == p * q
#     print('a=', a)
#     print('b=', b)
#     print('p=', p)
#     print('q=', q)
#     print('pq=', p*q)
#     return p, q
#
# n=103591*104729
# fermat(n)

# import os
#
#
# def get_path(filename):
#     """Return file's path or empty string if no path."""
#     head, tail = os.path.split(filename)
#     return head
