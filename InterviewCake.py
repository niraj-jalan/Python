def getProductsOfAllIntsExceptAtIndex(int_Array):
    aSize = len(int_Array)
    if aSize < 2:
        raise IndexError('Getting the product of numbers at other '
                         'indices requires at least 2 numbers')

    return_array = [None] * aSize

    # This is o(n)^2 algorithm
    for i, value in enumerate(int_Array):
        r_product = 1;
        for j in range(i + 1, aSize):
            r_product = r_product * int_Array[j] if int_Array[i] > 0 else r_product
        l_product = 1
        for j in range(0, i):
            l_product = l_product * int_Array[j] if int_Array[j] > 0 else l_product

        return_array[i] = l_product * r_product

    print(return_array)

    # this is O(N) algorithm but with 2N space.
    left_product = [None] * aSize
    for i in range(0, aSize):
        if i == 0:
            left_product[i] = 1
        else:
            left_product[i] = left_product[i - 1] * int_Array[i - 1] if int_Array[i - 1] > 0 else left_product[i - 1]

    right_product = [None] * aSize
    for i in range(aSize - 1, -1, -1):
        if i == aSize - 1:
            right_product[i] = 1
        else:
            right_product[i] = right_product[i + 1] * int_array[i + 1] if int_Array[i + 1] > 0 else right_product[i + 1]

    for i in range(0, aSize - 1):
        return_array[i] = left_product[i] * right_product[i]

    print(return_array)

    # this is modification to above to use only O(N) space
    product = 1
    for i in range(aSize - 1, -1, -1):
        left_product[i] *= product
        product *= int_Array[i]

    print(left_product)

    '''
    product = 1;
    for i in int_Array:
        print(i)
        product = product * i
    
    for index, i in enumerate(int_Array):
        print('i is %s At index %s'%(i, index))
    return_array[index] = product / i
    '''
    return return_array


int_array = [0, 1, 7, 3, 4]
print(getProductsOfAllIntsExceptAtIndex(int_array))
