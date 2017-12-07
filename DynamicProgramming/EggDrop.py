import sys

def findDrops(floors, eggs):
  if floors == 0 or floors == 1 or eggs == 1:
    return floors
  
  min_drops = sys.maxint
  for i in range(1, floors+1):
    no_of_drops = max(findDrops(i - 1, eggs -1), findDrops(floors - i, eggs))
    #print('Floors-%s , Eggs-%s, no_of_drop -%s'%(floors,eggs, no_of_drops))
    if min_drops > no_of_drops:
      min_drops = no_of_drops
 
  return min_drops + 1

#print(findDrops(100,2))


# Function to get minimum number of trials needed in worst
# case with n eggs and k floors
def eggDrop(k, n):
    # A 2D table where entery eggFloor[i][j] will represent minimum
    # number of trials needed for i eggs and j floors.
    eggFloor = [[0 for x in range(k+1)] for x in range(n+1)]
 
    # We need one trial for one floor and0 trials for 0 floors
    for i in range(1, n+1):
        eggFloor[i][1] = 1
        eggFloor[i][0] = 0
 
    # We always need j trials for one egg and j floors.
    for j in range(1, k+1):
        eggFloor[1][j] = j
 
    # Fill rest of the entries in table using optimal substructure
    # property
    for i in range(2, n+1):
        for j in range(2, k+1):
            eggFloor[i][j] = sys.maxint
            for x in range(1, j+1):
                res = 1 + max(eggFloor[i-1][x-1], eggFloor[i][j-x])
                if res < eggFloor[i][j]:
                    eggFloor[i][j] = res
 
    # eggFloor[n][k] holds the result
    return eggFloor[n][k]
  
#print(eggDrop(100,2))
