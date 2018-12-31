def function_a():
    global a
    a = 1
    b = 2
    return a+b


def function_b():
    c = 3
    return a+c


print(function_a())
print(function_b())


# def many(*args, **kwargs):
#     print(args)
#     print(kwargs)
#
#
# many(1, 2, 3, name="Mike", job="programmer")


# def keyword_function(a=1, b=2):
#     return a+b
#
#
# print(keyword_function(b=4, a=5))

# def add(a, b):
#     return a + b
#
#
# print(add(a=2, b=3))
# total = add(b=4, a=5)
# print(total)

# print(add(1, 2))
# add(1)
# def empty_function():
#     pass
#
#
# def a_function():
#     print("You just created a function!")
#
#
# # a_function()
# empty_function()
