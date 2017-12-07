import sys
from itertools import islice


def getProductsOfAllIntsExceptAtIndex(input_array):
    aSize = len(input_array)
    if aSize < 2:
        raise IndexError('Getting the product of numbers at other '
                         'indices requires at least 2 numbers')

    return_array = [None] * aSize

    # This is o(n)^2 algorithm
    for i, value in enumerate(input_array):
        r_product = 1
        for j in range(i + 1, aSize):
            r_product = r_product * input_array[j] if input_array[i] > 0 else r_product
        l_product = 1
        for j in range(0, i):
            l_product = l_product * input_array[j] if input_array[j] > 0 else l_product

        return_array[i] = l_product * r_product

    print(return_array)

    # this is O(N) algorithm but with 2N space.
    left_product = [None] * aSize
    for i in range(0, aSize):
        if i == 0:
            left_product[i] = 1
        else:
            left_product[i] = left_product[i - 1] * input_array[i - 1] if input_array[i - 1] > 0 else left_product[
                i - 1]

    right_product = [None] * aSize
    for i in range(aSize - 1, -1, -1):
        if i == aSize - 1:
            right_product[i] = 1
        else:
            right_product[i] = right_product[i + 1] * input_array[i + 1] if input_array[i + 1] > 0 else right_product[
                i + 1]

    for i in range(0, aSize - 1):
        return_array[i] = left_product[i] * right_product[i]

    print(return_array)

    # this is modification to above to use only O(N) space
    product = 1
    for i in range(aSize - 1, -1, -1):
        left_product[i] *= product
        product *= input_array[i]

    print(left_product)

    '''
    product = 1;
    for i in input_array:
        print(i)
        product = product * i
    
    for index, i in enumerate(input_array):
        print('i is %s At index %s'%(i, index))
    return_array[index] = product / i
    '''
    return return_array


# input_array = [0, 1, 7, 3, 4]
# print(getProductsOfAllIntsExceptAtIndex(input_array))


def getMaximumProductofThreeInArray(input_array):
    if len(input_array) < 3:
        raise Exception('Less than 3 items!')

    print(input_array)

    highest = max(input_array[0], input_array[1])
    lowest = min(input_array[0], input_array[1])

    highest_product_of_2 = input_array[0] * input_array[1]
    lowest_product_of_2 = input_array[0] * input_array[1]

    highest_product_of_3 = input_array[0] * input_array[1] * input_array[2]

    for current in islice(input_array, 2, None):
        highest_product_of_3 = max(highest_product_of_3, highest_product_of_2 * current, lowest_product_of_2 * current)
        highest_product_of_2 = max(highest_product_of_2, highest * current, lowest * current)
        lowest_product_of_2 = min(lowest_product_of_2, highest_product_of_2 * current, lowest * current)

        highest = max(highest, current)
        lowest = min(lowest, current)

    print(highest_product_of_3)

    min1, min2 = sys.maxint, sys.maxint
    max1, max2, max3 = -min1 - 1, -min1 - 1, -min1 - 1
    for i in input_array:
        if i <= min1:
            min2 = min1
            min1 = i
        elif min1 <= i <= min2:
            min2 = i

        if i >= max1:
            max3 = max2
            max2 = max1
            max1 = i
        elif max1 >= i >= max2:
            max3 = max2
            max2 = i
        elif max2 >= i >= max3:
            max3 = i

    # print('Minimums - %s, %s'%(min1,min2))
    #    print('Maximums - %s, %s, %s'%(max1,max2, max3))
    if min1 * min2 > max1 * max2:
        return min1 * min2 * max1
    elif min1 * min2 > max2 * max3:
        return min1 * min2 * max1
    else:
        return max1 * max2 * max3


# input_array = [-10, 4, 1, 3, 2, 0, 10, 5, 7, 8];
# print(getMaximumProductofThreeInArray(input_array))


def merge_calendar(list_of_tuples):
    # sort the list first to ensure all start times are sorted.
    list_of_tuples = sorted(list_of_tuples)
    start_time = None
    end_time = None
    out = []
    for x, y in list_of_tuples:
        # first iteration start_time and end_time are going to be none. Assign value and continue
        if start_time is None or end_time is None:
            start_time = x
            end_time = y
            continue

        # check if the new meeting is already within the time-span of old meeting. If yes then simply continue
        if start_time <= x and end_time >= y:
            continue

        # check if the start time of the meeting is between the start and end time of previous meeting; set the max end time
        if start_time <= x <= end_time:
            end_time = max(end_time, y)
        # if the meeting starts early and ends after the previous meeting starts, adjust the start time
        elif x <= start_time <= y:
            start_time = x
        # the two meetings dont overlap. Add the meeting to final cal, and update new start and end time
        else:
            out.append(tuple((start_time, end_time)))
            start_time = x
            end_time = y

    # add the final overlapped meeting to the list
    out.append(tuple((start_time, end_time)))
    print(out)


#merge_calendar(list_of_tuples=[(1, 2), (2, 3)])
#merge_calendar(list_of_tuples=[(1, 5), (2, 3)])
#merge_calendar(list_of_tuples=[(1, 10), (2, 6), (3, 5), (7, 9)])
#merge_calendar(list_of_tuples=[(3, 5), (4, 8), (10, 12), (0, 1), (9, 10)])


def calcMaxProfit(n):
  buy = None
  sell = None
  
  for price in n:
    if buy is not None and price < buy:
      print('buy at %s and sell at %s'%(buy,sell))
      buy, sell = price, None
    else:
      buy = price if buy is None else buy
      sell = price if sell < price else sell
   
  print('buy at %s and sell at %s'%(buy,sell))


calcMaxProfit(n = [100, 180, 260, 310, 40, 535, 695])
   





