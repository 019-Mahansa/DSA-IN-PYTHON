def recursion_func(n):
    if n == 0:
        return 1
    else:
        return n * recursion_func(n - 1)


print(recursion_func(5))