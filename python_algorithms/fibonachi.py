"""recursion example"""


def fibonacci(n):
    if n in (1, 2):
        return 1
    return fibonacci(n-1) + fibonacci(n-2)


print(fibonacci(1))
print(fibonacci(6))
print(fibonacci(10))

"""for example"""
# fib1 = fib2 = 1
# n = int(input("Please enter the number: "))
#
# if n < 2:
#     quit()
#
# print(fib1, end=' ')
# print(fib2, end=' ')
#
# for i in range(2, n):
#     fib1, fib2 = fib2, fib1 + fib2
#     print(fib2, end=' ')
#
# print()

"""2-nd example for while"""
# fib1 = fib2 = 1
#
# n = int(input("The element number of the Fibonacci series: "))
#
# while n > 0:
#     fib1, fib2 = fib2, fib1 + fib2
#     n -= 1
#
# print(fib2)

"""1-st example for while"""
# fib1 = 1
# fib2 = 1
#
# n = input("The element number of the Fibonacci series: ")
# n = int(n)
#
# i = 0
# while i < n - 2:
#     fib_sum = fib1 + fib2
#     fib1 = fib2
#     fib2 = fib_sum
#     i = i + 1
#
# print(fib2)
