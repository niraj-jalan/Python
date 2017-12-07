import sys

def findUgly(n):
  a = [None]*(n+1)
  a[0] =0
  a[1] = 1
  for i in range(1, n):
    print(a)
    if a[n] is not None:
      print(a[n])
      break
    
    if i*2 <= n and a[i*2] is None:
      a[i*2] = i*2
    if i*3 <= n and a[i*3] is None:
      a[i*3] = i*3
    if i*5 <= n and a[i*5] is None:
      a[i*5] = i*5
      
findUgly(7)
      
      