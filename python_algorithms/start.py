# Sum and products of digits
...

# And you came up with this function...


def sum2(n):
    """
    Take an input of n and return the sum of the numbers from 0 to n
    """
    result = (n*(n+1))/2
    return print(result)


# sum2(5)

# Imagine I came up with this function...


def sum1(n):
    """
    Take an input of n and return the sum of the numbers from 0 to n
    """
    final_sum = 0
    for x in range(n+1):
        final_sum += x

    return print(final_sum)


# sum(3)
