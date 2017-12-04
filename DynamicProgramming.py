import sys

sys.setrecursionlimit(2 * 10 ** 5)


class BearHairCut:
    def main(argv=None):
        for t in range(int(input())):
            n_spcl_days, start_day, end_day = map(int, input().split())
            spcl_days = list(map(int, input().split()))

            dp_array = []
            dp_array.append(0)
            t = []
            t.append(1);

            max_spcl_day = max(spcl_days)
            min_spcl_day = min(spcl_days)

            # print(max_spcl_day)
            for i in range(1, max_spcl_day + 2):
                dp_array.append(0);

            for i in range(1, max_spcl_day + 1):
                t.append(0)

            for i in spcl_days:
                # print(i)
                t[i] = 1

            for i in range(0, max_spcl_day + 1):
                # print('i = %s'%i)
                if i >= 1:
                    dp_array[i] = max(dp_array[i], dp_array[i - 1])

                cnt = 0;
                for j in range(i + start_day, min(i + end_day + 1, max_spcl_day + 1)):
                    # print(j)
                    if t[j] == 1:
                        cnt = cnt + 1
                    dp_array[j] = max(dp_array[j], dp_array[i] + cnt)

            dp_array[max_spcl_day + 1] = max(dp_array[max_spcl_day + 1], dp_array[max_spcl_day]);
            print(dp_array[max_spcl_day + 1])


#bear_haircut = BearHairCut()
#bear_haircut.main()


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



# A Naive recursive Python program to fin minimum number
# operations to convert str1 to str2
def editDistance(str1, str2, m , n):
 
    # If first string is empty, the only option is to
    # insert all characters of second string into first
    if m==0:
         return n
 
    # If second string is empty, the only option is to
    # remove all characters of first string
    if n==0:
        return m
 
    # If last characters of two strings are same, nothing
    # much to do. Ignore last characters and get count for
    # remaining strings.
    if str1[m-1]==str2[n-1]:
        return editDistance(str1,str2,m-1,n-1)
 
    # If last characters are not same, consider all three
    # operations on last character of first string, recursively
    # compute minimum cost for all three operations and take
    # minimum of three values.
    return 1 + min(editDistance(str1, str2, m, n-1),    # Insert
                   editDistance(str1, str2, m-1, n),    # Remove
                   editDistance(str1, str2, m-1, n-1)    # Replace
                   )
  
# A Dynamic Programming based Python program for edit
# distance problem
def editDistDP(str1, str2, m, n):
    # Create a table to store results of subproblems
    dp = [[0 for x in range(n+1)] for x in range(m+1)]
 
    # Fill d[][] in bottom up manner
    for i in range(m+1):
        for j in range(n+1):
 
            # If first string is empty, only option is to
            # isnert all characters of second string
            if i == 0:
                dp[i][j] = j    # Min. operations = j
 
            # If second string is empty, only option is to
            # remove all characters of second string
            elif j == 0:
                dp[i][j] = i    # Min. operations = i
 
            # If last characters are same, ignore last char
            # and recur for remaining string
            elif str1[i-1] == str2[j-1]:
                dp[i][j] = dp[i-1][j-1]
 
            # If last character are different, consider all
            # possibilities and find minimum
            else:
                dp[i][j] = 1 + min(dp[i][j-1],        # Insert
                                   dp[i-1][j],        # Remove
                                   dp[i-1][j-1])    # Replace
 
    return dp[m][n]

