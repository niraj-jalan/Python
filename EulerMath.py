import time
import math
import sys

sys.setrecursionlimit(2 * 10 ** 5)

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


'''
# This solution used sqrt function which takes addition logN time. The second solution to iterate over factor seems more efficient. 
def find_greatest_prime_factor(num):
    #print(num)
    # base condition - 
    if num < 3:
      return num
    # find the sqrt
    num_sqrt = math.ceil(math.sqrt(num))
    for i in xrange(int(num_sqrt), 1, -1):
      if num%i == 0:
        #check if i is prime
        if find_greatest_prime_factor(i) == i:
          return i
    #num is prime - return num
    return num
'''


def largest_prime_factor(num, div=2):
    while div < num:
        if num % div == 0 and num / div > 1:
            num = num / div
            div = 2
        else:
            div = div + 1
    return num


start_time = time.time()
# findMultiplesOf3and5(1000)
#print(fibonacci(4000000))
print(largest_prime_factor(600851475143))
print("This took", time.time() - start_time, "seconds to run.")
#start_time = time.time()
#print("This took", time.time() - start_time, "seconds to run.")

