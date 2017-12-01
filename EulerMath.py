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

def find_greatest_prime_factor(num):
    
    # base condition - 
    if num < 3:
      return num
    
    # find the sqrt
    num_sqrt = math.ceil(math.sqrt(num))
    #print(num_sqrt)
    for i in xrange(int(num_sqrt), 1, -1):
      if num%i == 0:
        #check if i is prime
        if find_greatest_prime_factor(i) == i:
          return i
    
    return num
  
start_time = time.time()
# findMultiplesOf3and5(1000)
#print(fibonacci(4000000))
print(find_greatest_prime_factor(32))
print("This took", time.time() - start_time, "seconds to run.")
