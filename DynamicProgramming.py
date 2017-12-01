def fibonacci(n, history):
    if n <= 1:
        return 1
    elif n in history:
        return history[n]
    else:
        fib = fibonacci(n - 1, history) + fibonacci(n - 2, history)
        history[n] = fib
        print(fib, end=',')
        return fib


def calc_ways_2_climb(n):
    if n < 0:
        return 0
    if n == 0:
        return 1
    return calc_ways_2_climb(n - 1) + calc_ways_2_climb(n - 2) + calc_ways_2_climb(n - 3)


# print(calc_ways_2_climb(3))
print(1, end=',')
fibonacci(30, history={})
