"""decorators"""


def decor_with_return(fn):
    def wrapper(*args, **kwargs):
        print("Run method: " + str(fn.__name__))
        return fn(*args, **kwargs)
    return wrapper


@decor_with_return
def calc_sqrt(val):
    return val**0.5

# def method_decor(fn):
#     def wrapper(self):
#         print("Run method: " + str(fn.__name__))
#         fn(self)
#     return wrapper
#
#
# class Vector:
#     def __init__(self, px=0, py=0):
#         self.px = px
#         self.py = py
#
#     @method_decor
#     def norm(self):
#         print((self.px**2 + self.py**2)**0.5)


# def param_transfer(fn):
#     def wrapper(arg):
#         print("Run function: " + str(fn.__name__) + "(), with param: " + str(arg))
#         fn(arg)
#     return wrapper
#
#
# @param_transfer
# def print_sqrt(num):
#     print(num**0.5)

# def simple_decore(fn):
#     def wrapper():
#         print("Run function")
#         fn()
#         print("Stop function")
#     return wrapper()
#
#
# @simple_decore
# def first_test():
#     print("Test function 1")
#
#
# @simple_decore
# def second_test():
#     print("Test function 2")

# def mul(a):
#     def helper(b):
#         return a * b
#     return helper

# class DemoCall():
#     def __call__(self):
#         return "Hello!"

# a = [1, 2, 3, 4, 5]
# sq = lambda x: x**2
# print(sq(5))
#
# b = list(map(sq, a))
# print(b)
