import time


def findMultiplesOf3and5(number):
    sum = 0
    for i in range(1, number):
        if i % 3 == 0 or i % 5 == 0:
            sum = sum + i

    print(sum)


def fibonacci(n):
    a, b = 0, 1
    sumValue = 0
    while b < n:
        a, b = b, a + b
        if b % 2 == 0:
            sumValue = sumValue + b

    return sumValue


start_time = time.time()
# findMultiplesOf3and5(1000)
print(fibonacci(4000000))
print("This took", time.time() - start_time, "seconds to run.")
