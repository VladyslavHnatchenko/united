"""import/from module"""
def hello():
    print("Hello, world!")


def fib(n):
    a = b = 1
    for i in range(n - 2):
        a, b = b, a + b
    return b


if __name__ == "__main__":
    hello()
    for i in range(10):
        print(fib(i))


# import math as m
#
#
# print(m.e)

# import time
# import random
#
#
# print(time.time())
# print(random.random())

# import os
# print(os.getcwd())

"""with as"""
# with open('1.txt', 'w', encoding='utf-8') as g:
#     d = int(input())
#     print('1 / {} = {}'.format(d, 1 / d), file=g)

# f = open('1.txt', 'r')
# lt = [line.strip() for line in f]
# print(lt)
# f.close()

# list_p = [str(i) + str(i-1) for i in range(20)]
# f = open('1.txt', 'w')
#
# for index in list_p:
#     f.write(index + '\n')
#
# f.close()

# f = open('1.txt', 'r')
# for line in f:
#     print(line)

"""exceptions"""
# f = open('1.txt')
# ints = []
# try:
#     for line in f:
#         ints.append(int(line))
# except ValueError:
#     print("This's not a number, exit!")
# except Exception:
#     print("WTF???")
# else:
#     print("All is good!")
# finally:
#     f.close()
#     print('I closed file.')

# try:
#     k = 1 / 0
# except ArithmeticError:
#     k = 0
#
#
# print(k)

# q = 100 / 0
# print(q)

"""function"""
# func = lambda x, y: x + y
# print(func(1, 2))
# print(func(22, 22))

# def func(**kwargs):
#     return kwargs
#
#
# print(func(a=1, b=2, c=3))

# def func(*args):
#     return args
#
#
# print(func(1, 2, 3, 'abc'))
# print(func())
# print(func(1))

# def new_func(n):
#     def my_func(x):
#         return x + n
#     return my_func
#
#
# new = new_func(100)
# print(new(22))

"""frozenset"""
# a = set('qwerty')
# b = frozenset('qwerty')
# print(a == b)
#
# print(type(a - b))
# a.add(1)
# b.add(1)

"""set"""
# a = set()
# print(a)
#
# b = set('hello')
# print(b)
#
# c = {'a', 'b', 'c', 'd'}
# print(c)
#
# d = {i ** 2 for i in range(10)}
# print(d)
#
# print(type(a))
# print(type(b))
# print(type(c))
# print(type(d))

"""dict"""
# d = {a: a**2 for a in range(7)}
# print(d)

# d = dict.fromkeys(['a', 'b'])
# print(d)
#
# d1 = dict.fromkeys(['a', 'b'], 100)
# print(d1)

# d = {}
# print(d)
#
# d1 = {'dict': 1, 'dictionary': 2}
# print(d1)
#
# d2 = dict(short='dict', long='dictionary')
# print(d2)

"""tuple"""
# a = tuple('hello, world!')
# print(a)

# a = ('s',)
# print(a)
# a = tuple()
# print(a)
#
# b = ()
# print(b)

# d = {(1, 1, 1): 1}
# d = {[1, 1, 1]: 1}

# a = (1, 2, 3, 4, 5, 6)
# b = [1, 2, 3, 4, 5, 6]
# print(a.__sizeof__())
# print(b.__sizeof__())

"""list"""
# a = [1, 3, 8, 7]
# a[1:3] = [0, 0, 0]
# print(a)

# a = [1, 3, 8, 7]
# print(a[::-1])
# print(a[:-2])
# print(a[-2::-1])
# print(a[1:4:-1])

# print(a[:])
# print(a[1:])
# print(a[:3])
# print(a[::2])

# list_p = [1, 2, 5, 9, 4, 5]
# list_p.sort()
# print(list_p)

# c = [c * 3 for c in 'list' if c != 'i']
# print(c)

# c = [c * 3 for c in 'list']
# print(c)

"""keywords"""
# False, True, None, and, with/as, assert, break, class, continue, def, del, elif,
# else, except, fina;;y, fpr, from, global, if, import, in, is, lambda, nonlocal,
# not, or, pass, raise, return, try, while, yield

"""for, while, break, continue, else"""
# for i in "hello world":
#     if i == "a":
#         break
# else:
#     print("We don't have letter 'a' in string")
# for i in "hello world":
#     if i == "o":
#         break
#     print(i * 2, end='')

# for i in "hello world":
#     if i == "o":
#         continue
#     print(i * 2, end='')

# for i in "hello world":
#     print(i * 2, end='')

# i = 5
# while i < 15:
#     print(i)
#     i = i + 2

"""if-elif-else"""
# a = int(input())
# if a < -5:
#     print("Low")
# elif -5 <= a <= 5:
#     print("Mid")
# else:
#     print("High")
